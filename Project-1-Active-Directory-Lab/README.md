# Enterprise Active Directory & PowerShell Automation Lab (Project 1)

##  Project Goal
The objective of this project was to architect, configure, and secure a private, isolated Enterprise Network Environment using Windows Server 2025 and Windows 11. The lab focuses on deploying Activ[...]

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
* **Screenshot Verification:** ![Active Directory Users and Computers](images/project1-01-ad-users-and-computers.png)

### Task 2: Client Workstation Integration
* **Action:** Coordinated system settings on the Windows 11 Virtual Machine to link it directly to the `lab.local` domain, verifying credentials against the server database.
* **Screenshot Verification:** *[Insert Screenshot of the Windows 11 Welcome popup window or System Properties showing domain status]*

### Task 3: Building Corporate Hierarchy
* **Action:** Created 3 distinct Organizational Units (OUs) named **HR**, **Finance**, and **IT**, and added department-specific security groups and initial seed accounts.
* **Screenshot Verification:** ![HR OU users](images/project1-02-ad-hr-ou.png)


![IT OU users](images/project1-04-ad-it-ou.png)

### Task 4: Hardening & Security Controls
* **Action:** Applied Group Policy Objects (GPOs) to mandate strict password complexity guidelines and a defensive Account Lockout Policy. Verified the rule via intentional client-side failure.
* **Screenshot Verification:** ![GPO Account Lockout](images/project1-03-gpo-account-lockout.png)

### Task 5: PowerShell Automation Loop
* **Action:** Authored and executed a PowerShell pipeline script (`import.ps1`) to parse a local CSV file database and dynamically batch-generate 20 employee profiles into their correct target OUs[...]
* **Screenshot Verification:** *[Insert Screenshot of PowerShell terminal showing the script running and the accounts populating AD]*

---

##  Project Metrics & Takeaways

###  Time Invested
* **Total Duration:** ~6 Hours

###  The Biggest Obstacle
* **The Problem:** The initially selected OS option defaulted to **Windows Server Core (CLI Only)** instead of the full graphical version. This completely stripped away the Server Manager dashboar[...]
* **The Resolution:** Safely removed the virtual partition and initiated a clean re-installation, ensuring **Windows Server 2025 Standard (Desktop Experience)** was highlighted. Developed standalo[...]

###  Core Lessons Learned
* **Infrastructure Dependencies:** Mastered how Active Directory relies heavily on precise DNS alignment; if a client's network adapter does not target the exact IP address of the Domain Controlle[...]
* **Security Layer Rules:** Learned the difference between local machine credential validation timers and centralized Domain Server Lockout GPOs.
* **The Power of Scripting:** Experienced how combining plain-text data parsing with programmatic arrays eliminates manual data entry mistakes, saving hours of system administrator work through au[...]
