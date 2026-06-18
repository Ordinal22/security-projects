# Security Projects Lab

This repository contains system automation and security auditing scripts developed to run safely in isolated environments.

## Included Tools

### 1. Automated File Lister (`file_lister.ps1`)
*   **Purpose**: Scans specified system folders to extract metadata, file sizes, and modification timestamps.
*   **Security Use Case**: Helps blue team analysts map out directory contents to audit files or quickly spot unexpected large files or changes.

### 2. Automatic Log Creator (`file_creator.ps1`)
*   **Purpose**: Instantly generates text files stamped with the exact system date and time.
*   **Security Use Case**: Simulates endpoint payload drops for defense testing, or builds automated incident log files during an investigation.
