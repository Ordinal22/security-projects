# Project 3: Windows Security Log Automation Tool

## Project Overview
This project is a lightweight, high-utility Python automation tool designed to ingest, parse, and analyze raw multi-line Windows Security event logs exported from a Splunk enterprise environment. The tool automatically evaluates authentication logs to detect potential security incidents, flag malicious brute-force attempts, and highlight critical account lockouts in real-time.

---

## Design Choices and Architecture
* **State Machine for Multi-Line Parsing**: Raw Windows Event Logs break single events into multi-line key-value stanzas rather than standard single-line strings. This script utilizes a custom state machine that chunks data cleanly via `LogName=` boundaries to securely preserve context across separate lines.
* **Enterprise Event Code Filtering**: Instead of relying on volatile keyword phrasing, the tool maps directly to immutable Windows Security log IDs:
  * **EventCode 4625**: Failed account logon.
  * **EventCode 4740**: Explicit security account lockout.
* **Corporate Noise Mitigation**: The parsing logic automatically filters out background system services (`SYSTEM`) and standard machine accounts (identifiable by trailing `$` characters), ensuring reports contain only actionable user telemetry.
* **Strict Scope Isolation**: In alignment with clean engineering principles, the tool intentionally avoids external databases, web wrappers, or artificial intelligence overhead. It relies entirely on native Python data structures (`dictionaries` and `lists`) for rapid, self-contained processing.

---

## Execution and Screenshot

### How to Run the Tool
Ensure your log file is saved as `sample_log.txt` in the root folder, then open your terminal and execute:

```powershell
python security_tool.py
```

### Production Terminal Report Output
```text
========================================
      SECURITY AUTOMATION REPORT
========================================

[!] SUSPICIOUS FAILED LOGINS:
    - User 'BWayne': 3 failed attempt(s) [POTENTIAL BRUTE FORCE]

[CRITICAL] ACCOUNT LOCKOUTS:
    - ALERT: Account Locked Out -> User: BWayne

========================================
```

---

## Project Metrics and Reflection

* **Time Spent**: Approximately 8.5 hours (including virtual machine setup, driver troubleshooting, configuration, script engineering, validation testing, and tons of troubleshooting in general).
* **The Biggest Problem**: The initial script engine expected data to sit cleanly on single lines and hunted for simple strings like `"failed login"`. However, the raw Splunk lab export generated enterprise multi-line Windows data blocks where the target username and the `EventCode` sat entirely on separate rows, resulting in an empty report with zero detections.
* **How It Was Fixed**: The tool was completely refactored to read the log file into memory as complete blocks using a `.split()` method anchored on the `LogName` field. String-slicing logic was implemented via indices to cleanly isolate data values after `EventCode=` and `Account Name:` indicators, allowing the script to flawlessly connect tracking variables across multi-line strings.

---

## Future Enhancements
Given additional time and expanded project scope, the following architecture upgrades would be implemented:
1. **Dynamic Argument Parsing**: Integrate Python's native `argparse` module to let security analysts specify custom log input paths and custom brute-force event count thresholds straight from the command line interface.
2. **Standardized JSON Export Engine**: Add a secondary reporting output function that writes flagged security alerts to a standardized JSON format file for easy integration with security orchestration systems (SOAR).
