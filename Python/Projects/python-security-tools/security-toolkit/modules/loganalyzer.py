from pathlib import Path
from collections import Counter


def read_log(path):
    try:
        with open(path,"r") as file:
            return file.readlines()
        
    except FileNotFoundError:
        print("Log file not found")
        return []
    
def analyze_logs(lines):

    failed = 0
    success = 0
    ips = []

    for line in lines:

        if "FAILED" in line:
            failed += 1

        if "SUCCESS" in line:
            success += 1
        
        if "ip=" in line:
            ip = line.split("ip=")[1].strip()
            ips.append(ip)

    return failed, success, ips

def count_ips(ip_list):
    return Counter(ip_list)

def generate_report(failed, success, counts):
    report = ""
    report += "SECURITY LOG REPORT\n"
    report += "=" * 40 + "\n"

    report += f"Successful logins: {success}\n"
    report += f"Failed logins: {failed}\n\n"

    report += "IP Activity:\n"

    for ip, count in counts.items():
        report += f"{ip}: {count} events\n"
    
        if count >= 3:
            report += "Potential brute force detected\n"

    return report

def save_report(report):
    with open("report.txt", "w") as file:
        file.write(report)

def run_analyze_log():

    file_path = "sample.log"

    lines = read_log(file_path)

    if not lines:
        return "No log data found"

    failed, success, ips = analyze_logs(lines)

    counts = count_ips(ips)

    report = generate_report(
        failed,
        success,
        counts
    )

    save_report(report)

    return report