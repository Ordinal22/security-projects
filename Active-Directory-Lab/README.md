# Enterprise Active Directory & PowerShell Automation Lab (Project 1)

##  Project Goal
The objective of this project was to architect, configure, and secure a private, isolated Enterprise Network Environment using Windows Server 2025 and Windows 11. The lab focuses on deploying Active Directory Domain Services (AD DS), configuring network infrastructure, enforcing corporate Group Policies, and using PowerShell script loops to automate bulk employee account management.

---

##  Network Architecture Diagram
Below is the logical structure of the isolated lab environment:

```text
[ Windows Server 2025 GUI ]             [ Windows 11 Workstation ]
      (Domain Controller)                      (Domain Client)
         Domain: lab.local
     Static IP: 192.168.10.10  <=======>   Static IP: 192.168.10.20
     Subnet Mask: 255.255.255.0            Subnet Mask: 255.255.255.0
     DNS Server: 127.0.0.1                 DNS Server: 192.168.10.10
              ||                                     ||
              ====================  ===================
                                  ||
                        [ VirtualBox Internal Network ]
                                  (intnet)
```

---

##  Task Summaries & Screen Captures

### Task 1: Domain Controller Deployment
* **Action:** Installed the **Active Directory Domain Services** role on Windows Server 2025 and promoted it to a Domain Controller for the new forest root `lab.local`.
* **Screenshot Verification:** *[Insert Screenshot of "Active Directory Users and Computers" showing the root lab.local domain tree]*

### Task 2: Client Workstation Integration
* **Action:** Coordinated system settings on the Windows 11 Virtual Machine to link it directly to the `lab.local` domain, verifying credentials against the server database.
* **Screenshot Verification:** *[Insert Screenshot of the Windows 11 Welcome popup window or System Properties showing domain status]*

### Task 3: Building Corporate Hierarchy
* **Action:** Created 3 distinct Organizational Units (OUs) named **HR**, **Finance**, and **IT**, and added department-specific security groups and initial seed accounts.
* **Screenshot Verification:** *[Insert Screenshot of HR OU folder displaying your manual user accounts and security groups]*

### Task 4: Hardening & Security Controls
* **Action:** Applied Group Policy Objects (GPOs) to mandate strict password complexity guidelines and a defensive Account Lockout Policy. Verified the rule via intentional client-side failure.
* **Screenshot Verification:** *[Insert Screenshot of Group Policy Management Editor showing your Account Lockout Threshold configurations]*

### Task 5: PowerShell Automation Loop
* **Action:** Authored and executed a PowerShell pipeline script (`import.ps1`) to parse a local CSV file database and dynamically batch-generate 20 employee profiles into their correct target OUs.
* **Screenshot Verification:** *[Insert Screenshot of PowerShell terminal showing the script running and the accounts populating AD]*

---

##  Project Metrics & Takeaways

###  Time Invested
* **Total Duration:** ~6 Hours

###  The Biggest Obstacle
* **The Problem:** The initially selected OS option defaulted to **Windows Server Core (CLI Only)** instead of the full graphical version. This completely stripped away the Server Manager dashboard and visual consoles needed to follow the lab steps, forcing configuration changes exclusively via PowerShell cmdlets. Additionally, the isolated internal network cut off external internet capabilities, making it impossible to download setup sheets from the web.
* **The Resolution:** Safely removed the virtual partition and initiated a clean re-installation, ensuring **Windows Server 2025 Standard (Desktop Experience)** was highlighted. Developed standalone, self-generating computer math loop arrays in local PowerShell (`1..20 | ForEach-Object {...}`) to construct the local CSV spreadsheets instantly from scratch inside the network partition without needing external downloads or copy-paste clipboards.

###  Core Lessons Learned
* **Infrastructure Dependencies:** Mastered how Active Directory relies heavily on precise DNS alignment; if a client's network adapter does not target the exact IP address of the Domain Controller, domain authentication completely drops.
* **Security Layer Rules:** Learned the difference between local machine credential validation timers and centralized Domain Server Lockout GPOs.
* **The Power of Scripting:** Experienced how combining plain-text data parsing with programmatic arrays eliminates manual data entry mistakes, saving hours of system administrator work through automation.
