import os

def analyze_security_logs(file_path):
    if not os.path.exists(file_path):
        print(f"[ERROR] The file at '{file_path}' does not exist.")
        return

    failed_logins = {}  
    lockouts = []       

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as log_file:
            # Read the whole file content to parse standalone event blocks cleanly
            content = log_file.read()
            
        # Split chunks whenever a new date/time stamp log entry initializes
        # Since text files vary, splitting by LogName or EventCode entries works best
        events = content.split("LogName=")
        
        for event in events:
            if not event.strip():
                continue
                
            lines = event.split("\n")
            event_code = None
            user = None
            
            for line in lines:
                clean = line.strip()
                if clean.startswith("EventCode="):
                    event_code = clean.split("=")[1].strip()
                elif clean.startswith("Account Name:"):
                    parts = clean.split(":")
                    if len(parts) > 1:
                        val = parts[1].strip()
                        if val and not val.endswith("$") and val.lower() != "system":
                            user = val

            if event_code and user:
                if event_code == "4625":
                    failed_logins[user] = failed_logins.get(user, 0) + 1
                elif event_code == "4740":
                    if user not in lockouts:
                        lockouts.append(user)

        print_security_report(failed_logins, lockouts)

    except Exception as e:
        print(f"[CRITICAL] Error reading logs: {e}")

def print_security_report(failed_dict, lockout_list):
    print("\n" + "="*40)
    print("      SECURITY AUTOMATION REPORT      ")
    print("="*40)
    
    print("\n[!] SUSPICIOUS FAILED LOGINS:")
    if not failed_dict:
        print("    - No failed login attempts detected.")
    else:
        for user, count in failed_dict.items():
            flag = "[POTENTIAL BRUTE FORCE]" if count >= 3 else ""
            print(f"    - User '{user}': {count} failed attempt(s) {flag}")

    print("\n[CRITICAL] ACCOUNT LOCKOUTS:")
    if not lockout_list:
        print("    - Zero account lockouts detected.")
    else:
        for user in lockout_list:
            print(f"    - ALERT: Account Locked Out -> User: {user}")
            
    print("\n" + "="*40)

if __name__ == "__main__":
    LOG_PATH = "capstone_logs.txt" 
    analyze_security_logs(LOG_PATH)
