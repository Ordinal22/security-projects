# Security Projects Portfolio

> A comprehensive collection of enterprise-grade security infrastructure, threat detection, and log automation projects developed in isolated lab environments.

**GitHub Profile:** [@Ordinal22](https://github.com/Ordinal22) | **Total Time Invested:** 20+ hours | **Environment:** Oracle VirtualBox (Isolated Networks)

---

## Overview

This portfolio demonstrates hands-on expertise in **systems administration**, **security operations**, **threat detection**, and **automation engineering**. Each project showcases practical skills through real-world attack simulations, SIEM deployment, and end-to-end security workflows.

**Target Audience:** Security teams, infrastructure engineers, and technical interviewers

---

## Projects

### [Project 1: Enterprise Active Directory & PowerShell Automation Lab](./Project-1-Active-Directory-Lab/)

**Skills Demonstrated:** Active Directory, Group Policy, PowerShell Scripting, Windows Server Administration, Security Hardening

Deploy an isolated enterprise network infrastructure featuring Windows Server 2025 as a Domain Controller and Windows 11 as a domain-joined client. This project covers:

- **Active Directory Deployment**: Designed and implemented a complete AD forest with organizational units (OUs) for HR, Finance, and IT departments
- **Group Policy Hardening**: Applied security-focused GPOs including password complexity requirements and account lockout policies
- **PowerShell Automation**: Developed scripts to dynamically generate 20 employee profiles with proper OU assignments and group memberships
- **Network Architecture**: Established isolated internal network with static DNS and proper DNS resolution

**Key Takeaway:** Understand how modern enterprises manage user accounts, enforce security policies at scale, and use scripting to eliminate manual administrative overhead.

 **Time: ~6 hours** | 📁 [View Project](./Project-1-Active-Directory-Lab/)

---

### [Project 2: Centralized Security Log Analysis & SIEM Deployment](./Project-2-Splunk-SIEM-Lab/)

**Skills Demonstrated:** SIEM Administration, Security Event Monitoring, Threat Detection, Log Analysis, Splunk, Network Security

Deploy a centralized log ingestion and analysis platform using Splunk to monitor Windows domain infrastructure. This project demonstrates real-world threat detection capabilities:

- **Attack Simulation & Detection**: Executed brute-force attacks and privilege escalation attempts, then validated Splunk's ability to detect them via Windows Security Event Logs (Events 4625, 4740, 4720, 4728)
- **Log Correlation**: Learned how to correlate multiple event types to identify malicious patterns—individual failed logins are benign, but bursts of 4625 events preceding a 4624 reveal successful compromise
- **Network Configuration**: Overcame infrastructure challenges to establish secure log forwarding over port 9997 from endpoints to the central SIEM server
- **Event Field Mapping**: Extracted and analyzed critical fields like `TargetUserName`, `IpAddress`, and `Group_Name` to build investigative timelines

**Key Takeaway:** SIEM platforms are force multipliers for security teams, allowing analysts to see patterns across thousands of events that would be invisible in raw logs.

 **Time: 6+ hours** | 📁 [View Project](./Project-2-Splunk-SIEM-Lab/)

---

### [Project 3: Windows Security Log Automation Tool](./Project-3-Log-Automation/)

**Skills Demonstrated:** Python Development, Parsing & Regex, Security Automation, Data Analysis, Software Engineering

Build a lightweight Python automation tool to ingest, parse, and analyze raw Windows Security event logs exported from enterprise SIEM environments. This project showcases:

- **Multi-Line Log Parsing**: Developed a state machine-based parser to handle Windows Security logs that span multiple lines, using anchors on the `LogName` field to define event boundaries
- **Enterprise Event Filtering**: Implemented filtering logic to isolate critical events (EventCode 4625 for failed logins, 4740 for lockouts) while suppressing noise from system service accounts
- **Threat Detection Logic**: Built heuristics to identify brute-force patterns and account lockouts with detailed alert reporting
- **Clean Architecture**: Avoided over-engineering; the tool relies on pure Python, making it portable and maintainable without external dependencies

**Example Output:**
```
========================================
      SECURITY AUTOMATION REPORT
========================================

[!] SUSPICIOUS FAILED LOGINS:
    - User 'BWayne': 3 failed attempt(s) [POTENTIAL BRUTE FORCE]

[CRITICAL] ACCOUNT LOCKOUTS:
    - ALERT: Account Locked Out -> User: BWayne
```

**Key Takeaway:** Security automation doesn't require bloated frameworks—well-engineered tools using fundamentals (parsing, state machines, filtering) can deliver high value.

 **Time: ~8.5 hours** | 📁 [View Project](./Project-3-Log-Automation/)

---

### [Project 4: Mini-SOC Capstone – Automated Brute-Force Detection Pipeline](./Project4-4-Mini-SOC-Capstone/)

**Skills Demonstrated:** End-to-End Security Operations, Threat Hunting, Incident Response, Infrastructure Integration, Python Automation

Integrate all three previous projects into a complete Security Operations Center (SOC) workflow. This capstone project simulates a multi-stage brute-force attack pipeline:

- **Attack Generation**: Simulated credential attack against a domain user account
- **Telemetry Ingestion**: Windows Domain Controller generated authentication event logs and forwarded them to Splunk
- **SIEM Detection**: Validated Splunk's detection of brute-force patterns (Event 4625 spike, followed by Account Lockout Event 4740)
- **Automated Triage**: Python automation script parsed raw logs, isolated anomalies, and generated executive-ready security report

**End-to-End Proof:** Malicious activity generated → Splunk detected → Python triaged

 **Time: ~2 hours** | 📁 [View Project](./Project4-4-Mini-SOC-Capstone/)

---

## Technical Highlights

| Area | Technologies | Competencies |
|------|--------------|--------------|
| **Infrastructure** | Windows Server 2025, Active Directory, Group Policy, VirtualBox | Enterprise network design, domain administration, security hardening |
| **Threat Detection** | Splunk, Windows Security Event Logs, SIEM | Log analysis, attack simulation, event correlation, threat hunting |
| **Automation** | PowerShell, Python | Scripting, data parsing, automation frameworks, software engineering |
| **Security** | Brute-force detection, privilege escalation, account lockout policies | Defensive posture, incident response concepts, attack pattern recognition |

---

## What You'll Learn

By reviewing these projects, you'll see:

1. **Problem-Solving Under Constraints**: Each project involved technical obstacles (network isolation, driver issues, log formatting). The documentation shows how they were diagnosed and resolved
2. **Enterprise Thinking**: Real-world concerns like DNS resolution, account lockout policies, centralized logging, and noise reduction are baked into each project
3. **Documentation & Communication**: Each project is thoroughly documented with architecture diagrams, step-by-step actions, and key takeaways—skills crucial for team environments
4. **Systems Thinking**: Understanding how components (AD, Group Policy, SIEM, Python scripts) integrate into a cohesive security posture

---

## Getting Started

1. **Start with [Project 1](./Project-1-Active-Directory-Lab/)** if you're new to Active Directory or enterprise infrastructure
2. **Move to [Project 2](./Project-2-Splunk-SIEM-Lab/)** to see SIEM concepts in action and understand threat detection
3. **Explore [Project 3](./Project-3-Log-Automation/)** to see how automation bridges manual work and sophisticated tooling
4. **Wrap up with [Project 4](./Project4-4-Mini-SOC-Capstone/)** to see the full integration

Each project folder contains a detailed README with:
- Project goals and architecture diagrams
- Step-by-step implementation details
- Lessons learned and troubleshooting notes
- Screenshots and evidence of completion

---

## Interview Talking Points

Be ready to explain:

- **Why** certain design choices were made (e.g., why Splunk over ELK?)
- **How** you diagnosed and fixed problems (network isolation, log parsing challenges, firewall rules)
- **What** you'd do differently with more time or resources (scaling to 500 endpoints, live Splunk API integration)
- **Real-world applications** of each skill (AD groups for access control, SIEM correlation for threat hunting, Python for SOC automation)

---

## Contact & Next Steps

This portfolio is designed for **technical interviews, hiring managers, and security professionals**. Each project is a conversation starter backed by documented evidence.

For questions or deeper dives into any project, refer to the individual README files.

---

**Last Updated:** August 2026  
**Repository:** [Ordinal22/security-projects](https://github.com/Ordinal22/security-projects)  
**GitHub Profile:** [@Ordinal22](https://github.com/Ordinal22)
