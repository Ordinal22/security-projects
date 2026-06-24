Quick Recall Note: I set up Splunk on a Windows Domain Controller (.10) and a Windows 11 endpoint (.20). They talk on port 9997 on an Internal Network. I simulated brute-force attacks (Event 4625/4740) and admin privileges (Event 4728) and found them in Splunk.
# Project 3: Centralized Security Log Analysis & SIEM Deployment

##  Project Overview
Deployed an isolated enterprise-grade network infrastructure utilizing a Windows Server Domain Controller and a Windows 11 endpoint within Oracle VirtualBox. Configured centralized log ingestion using **Splunk Enterprise** and the **Splunk Universal Forwarder** to monitor, track, and alert on critical authentication events and administrative privilege changes.

*   **Time Spent:** 6+ Hours (Spread across environment staging, troubleshooting, and simulation loops)

---

##  Attack Simulations & Splunk Detections

### 1. Brute-Force & Account Lockout Tracking
*   **Simulation Action:** Executed an interactive brute-force attempt on the Windows 11 workstation endpoint, cycling bad credentials sequentially to intentionally trigger a local account lockout.
*   **Splunk Detection Metrics:** 
    *   **Event ID 4625 (Failed Login):** Extracted the `TargetUserName` parameter to identify the targeted account and parsed `IpAddress` to pinpoint the origin workstation.
    *   **Event ID 4740 (Account Lockout):** Tracked database updates utilizing the query `index=* EventCode=4740`. Inspected the `Target_Account_Name` field to confirm account mitigation and `Caller_Computer_Name` to identify the host execution source.

### 2. Unauthorized Persistence & Privilege Escalation
*   **Simulation Action:** Utilized Active Directory Users and Computers on the Domain Controller to create a new user profile (`TargetUser`) and immediately modified group memberships to elevate them into the `Domain Admins` organizational group.
*   **Splunk Detection Metrics:**
    *   **Event ID 4720 (User Creation):** Detected account creation anomalies using the query `index=* (EventCode=4720 OR EventCode=4728)`.
    *   **Event ID 4728 (Group Membership Change):** Expanded the event mapping block to isolate critical audit trail fields:
        *   `Account_Name`: Confirmed the change was executed by the `Administrator` account.
        *   `Group_Name`: Caught the target elevation to `Domain Admins` explicitly.

---

##  Key Takeaways: How Logs Reveal Malicious Activity
*   **Correlation is Key:** Individual event logs like successful logins (4624) are benign baselines, but when closely correlated with prior dense bursts of failed logins (4625), they reveal a successful brute-force compromise.
*   **Persistence Tracking:** Security event logs act as an immutable paper trail. Even if a threat actor creates a backdoored account and deletes their command history, Event ID 4720 permanently records the timestamp, the target username, and the specific administrative account used to create it.

---

##  Major Challenges & Technical Remediations

### 1. The Isolation vs. Ingestion Network Paradox
*   **The Problem:** Active Directory domain controllers require locked static local DNS paths (`127.0.0.1`) on an isolated internal network to prevent configuration interference. However, this cut off all external internet access, preventing the virtual machines from downloading the necessary Splunk installation packages.
*   **The Resolution:** Developed a multi-stage network routing bypass. Temporarily flipped the VM hypervisor settings to **NAT** and transitioned network card adapters to automated DHCP tracking to capture the ~1GB Splunk Enterprise payload. Once staged, flipped adapters back to **Internal Network**, restored static laboratory routing blocks (`192.168.10.10`), and successfully restored domain integrity.

### 2. Administrative Share File Pipeline Transfer Block
*   **The Problem:** The physical host PC was operating under restricted local guest user policies, meaning external utilities like ISO creators or VirtualBox Guest Additions drivers could not be installed to allow file transfers into the VM. 
*   **The Resolution:** Leveraged active domain trust paths. Dropped the lightweight Universal Forwarder payload onto the Server, opened an **Administrative Network Share backdoor (`\\192.168.10.10\c$`)** inside the Windows 11 Run dialog, and securely authenticated over the internal network to drop the installer right onto the workstation desktop without touching the host machine's restricted storage layer.

### 3. Local Endpoint Logging Silo
*   **The Problem:** The Windows 11 forwarder successfully connected to the server via network ping, but data indexes remained blank (`host 1`), hiding the endpoint's events due to Windows Server blocking port `9997` natively and a configuration file bug during installation.
*   **The Resolution:** Executed a two-pronged administrative change. Applied an inbound firewall rule via Server PowerShell (`New-NetFirewallRule -LocalPort 9997`) to permit clean log parsing. Then, accessed the underlying file structure inside the endpoint VM manually via Notepad (`C:\Program Files\SplunkUniversalForwarder\etc\system\local\inputs.conf`), explicitly forcing the log channels (`disabled = 0`) open. Forced a service cycle (`Restart-Service SplunkForwarder`), expanding server visibility immediately to `host 2`.

---

##  Dashboard Visualizations
*(Note: Drag and drop your project screenshots directly into this space on GitHub!)*

*   `[Insert Your Consolidated SOC Dashboard Screenshot Here]`
*   `[Insert Your Expanded Event 4728 Evidence Field Screenshot Here]`
