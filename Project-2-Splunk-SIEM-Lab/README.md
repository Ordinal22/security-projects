# (Quick Recall Note: I set up Splunk on a Windows Domain Controller (.10) and a Windows 11 endpoint (.20). They talk on port 9997 on an Internal Network. I simulated brute-force attacks (Event 462[...]

# Project 2: Centralized Security Log Analysis & SIEM Deployment

##  Project Overview
Deployed an isolated enterprise-grade network infrastructure utilizing a Windows Server Domain Controller and a Windows 11 endpoint within Oracle VirtualBox. Configured centralized log ingestion us[...]

*   **Time Spent:** 6+ Hours (Spread across environment staging, troubleshooting, and simulation loops)

---

##  Attack Simulations & Splunk Detections

### 1. Brute-Force & Account Lockout Tracking
*   **Simulation Action:** Executed an interactive brute-force attempt on the Windows 11 workstation endpoint, cycling bad credentials sequentially to intentionally trigger a local account lockout[...]
*   **Splunk Detection Metrics:** 
    *   **Event ID 4625 (Failed Login):** Extracted the `TargetUserName` parameter to identify the targeted account and parsed `IpAddress` to pinpoint the origin workstation.
    *   **Event ID 4740 (Account Lockout):** Tracked database updates utilizing the query `index=* EventCode=4740`. Inspected the `Target_Account_Name` field to confirm account mitigation and `Cal[...]

### 2. Unauthorized Persistence & Privilege Escalation
*   **Simulation Action:** Utilized Active Directory Users and Computers on the Domain Controller to create a new user profile (`TargetUser`) and immediately modified group memberships to elevate [...]
*   **Splunk Detection Metrics:**
    *   **Event ID 4720 (User Creation):** Detected account creation anomalies using the query `index=* (EventCode=4720 OR EventCode=4728)`.
    *   **Event ID 4728 (Group Membership Change):** Expanded the event mapping block to isolate critical audit trail fields:
        *   `Account_Name`: Confirmed the change was executed by the `Administrator` account.
        *   `Group_Name`: Caught the target elevation to `Domain Admins` explicitly.

---

##  Key Takeaways: How Logs Reveal Malicious Activity
*   **Correlation is Key:** Individual event logs like successful logins (4624) are benign baselines, but when closely correlated with prior dense bursts of failed logins (4625), they reveal a suc[...]
*   **Persistence Tracking:** Security event logs act as an immutable paper trail. Even if a threat actor creates a backdoored account and deletes their command history, Event ID 4720 permanently [...]

---

##  Major Challenges & Technical Remediations

### 1. The Isolation vs. Ingestion Network Paradox
*   **The Problem:** Active Directory domain controllers require locked static local DNS paths (`127.0.0.1`) on an isolated internal network to prevent configuration interference. However, this cu[...]
*   **The Resolution:** Developed a multi-stage network routing bypass. Temporarily flipped the VM hypervisor settings to **NAT** and transitioned network card adapters to automated DHCP tracking [...]

### 2. Administrative Share File Pipeline Transfer Block
*   **The Problem:** The physical host PC was operating under restricted local guest user policies, meaning external utilities like ISO creators or VirtualBox Guest Additions drivers could not be [...]
*   **The Resolution:** Leveraged active domain trust paths. Dropped the lightweight Universal Forwarder payload onto the Server, opened an **Administrative Network Share backdoor (`\\192.168.10.1[...]

### 3. Local Endpoint Logging Silo
*   **The Problem:** The Windows 11 forwarder successfully connected to the server via network ping, but data indexes remained blank (`host 1`), hiding the endpoint's events due to Windows Server [...]
*   **The Resolution:** Executed a two-pronged administrative change. Applied an inbound firewall rule via Server PowerShell (`New-NetFirewallRule -LocalPort 9997`) to permit clean log parsing. Th[...]

---

##  Dashboard Visualizations
*(Note: Drag and drop your project screenshots directly into this space on GitHub!)*

*   ![SOC Dashboard](images/project2-01-soc-dashboard.png)
*   ![Event 4728 evidence field](images/project2-02-event-4728.png)
