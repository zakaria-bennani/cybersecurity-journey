import argparse
import subprocess
import os 
from datetime import datetime 

def run_command(command):
    try:
        result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
        return result.stdout
    
    except Exception as e:
        return f"Error: {e}"
    
def get_recent_logs(lines):
    result = run_command(["journalctl", "-n", str(lines)])
    return result

def find_failed_logins(raw_logs):
    failed_events = []
    failed_total = 0
    for line in raw_logs.splitlines():
        if "failed" in line.lower() or "failure" in line.lower() or "authentication failure" in line.lower():
            failed_events.append(line)
    return len(failed_events)

def count_repeated_events(raw_logs):
    failed_count = 0
    auth_count = 0

    for line in raw_logs.splitlines():

        if "failed" in line.lower():
            failed_count += 1

        elif "authentication" in line.lower():
            auth_count += 1

    if failed_count + auth_count == 0:
        return 0, 0
        
    return failed_count, auth_count

def generate_findings(auth_count):
    
    if auth_count == 0: 
        return "No authentication failures detected."
    
    elif auth_count >=5:
        return f"High Number of failed login attempts detected. Total events: {auth_count}"
    
    else:
        return f"Repeated authentication failures warrant investigation. Total events: {auth_count}"

def save_report(lines_to_analyze):
    recent_logs = get_recent_logs(lines_to_analyze)
    failed_total = find_failed_logins(recent_logs)
    failed_count, auth_count = count_repeated_events(recent_logs)
    findings = generate_findings(auth_count)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    os.makedirs("reports", exist_ok=True)

    with open(f"reports/log_report_{timestamp}.txt","w") as file:
        file.write("="*20)
        file.write("\nLINUX LOG ANALYSIS REPORT\n")
        file.write("="*20 +"\n")
        file.write(f"\nDate: {timestamp}")
        file.write(f"\nLogs Analyzed: {lines_to_analyze}")
        file.write(f"\nFailed Login Count : {failed_total}" )
        file.write("\nRepeated Events: "+ f"\nFailed password: {failed_count}\n Authentication failure: {auth_count}") 
        file.write(f"\nFindings: {findings}"+"\n")
    
    print("Security report generated successfully in reports/ folder!")

def main():

    parser = argparse.ArgumentParser(
        description="Security Log Analyzer Tool"
    )

    parser.add_argument(
        "--lines",
        type=int,
        default=200,
        help="Write an Integer of how many logs you want to analyze "
    )

    args = parser.parse_args()

    save_report(args.lines)


if __name__ == "__main__":

    main()