import getpass
import platform 
import subprocess 
from datetime import datetime 

def get_user():
    return getpass.getuser()

def get_hostname():
    return platform.node()

def get_time():
    return datetime.now()

def run_command(command): 
    try:
        result = subprocess.run(
            command, 
            capture_output=True, 
            text = True
        )

        return result.stdout

    except Exception as e:
        return f"Error: {e}"

def run_sysinfo():

    report = ""

    report += "SYSTEM INFORMATION\n"
    report += "=" * 30 + "\n"

    report += f"User: {get_user()}\n"
    report += f"Hostname: {get_hostname()}\n"
    report += f"Time: {get_time()}\n"

    return report    