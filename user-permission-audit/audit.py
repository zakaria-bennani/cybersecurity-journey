import argparse
import subprocess
from datetime import datetime
import os

def run_command(command):
    try:
        result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
        return result.stdout
    
    except Exception as e:
        return ""

def get_current_user():
    return run_command(["whoami"])

def get_groups():
    return run_command(["groups"])

def get_login_accounts():
    result = run_command(["getent", "passwd"])

    login_accounts = []

    for line in result.splitlines():
        shell = line.split(":")[-1]
        if "nologin" not in shell and "false" not in shell:
            username = line.split(":")[0]
            login_accounts.append(username)
    return login_accounts

def get_sudo_user():
    result = run_command(["getent", "group", "sudo"])

    sudo_users = []
    for line in result.splitlines():
        members = line.split(":")[-1]
        sudo_users = members.split(",")
    sudo_count = len(sudo_users)
    return sudo_users, sudo_count
    

def find_world_writable():
    result = run_command(
        ["find", ".", "-maxdepth", "3", "-perm", "-002", "-type", "f"]
        )

    files = result.splitlines()
    return len(files), files
    

def generate_findings(sudo_count,ww_count):
    findings = []
    if sudo_count == 0:
        findings.append("No sudo users detected")
    elif sudo_count >= 3:
        findings.append("Multiple privilged accounts present")

    if ww_count >=20:
        findings.append("Review world-writable files for unnecessary exposure.")
    
    if not findings:
        findings.append("No critical findings")
    
    return "\n".join(findings)

def save_report(output_dir):
    current_user = get_current_user()
    groups = get_groups()
    login_accounts = get_login_accounts()
    sudo_users, sudo_count = get_sudo_user()
    ww_count, world_writable = find_world_writable()
    findings = generate_findings(sudo_count, ww_count)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    os.makedirs("reports", exist_ok=True)

    with open(f"{output_dir}/audit_{timestamp}.txt","w") as file:
        file.write("="*20)
        file.write("\nUSER AUDIT REPORT\n")
        file.write("="*20 +"\n")
        file.write("\nDate: "+ datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n")
        file.write("\nCurrent User: " + current_user +"\n")
        file.write("\nGroups: "+ groups +"\n")
        file.write("\nAccounts With Login Shells: \n"+ "\n".join(login_accounts) +"\n")
        file.write("\nPrivileged Users: "+ "\n".join(sudo_users) +"\n")
        file.write("\nWorld Writable Files: "+ "\n".join(world_writable) +"\n")
        file.write("\nFindings: " + findings + "\n")
    
    print("Report saved successfully.")




    

def main():
    parser = argparse.ArgumentParser(
    description="System Security Audit Tool"
    )

    parser.add_argument("--output-dir")
    args = parser.parse_args()
    save_report(args.output_dir)
        

if __name__ == "__main__":
    main()
