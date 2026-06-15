import platform #give you the machines info. What computer?
import subprocess #can make you run terminal commands using python
import getpass
from datetime import datetime #gives you the current time and date
import getpass

def get_user():
    return getpass.getuser()

def get_hostname():
    return platform.node() #hostname

def get_time():
    return datetime.now() #date and time

def run_command(command): 
    try: #telling python to not end the code if crashes but handle and tell us the error found
        result = subprocess.run(
            command, #whatever is told to do executes (e.g hostname -I )
            capture_output=True, #tells to save the output to use it in python
            text = True #return the output as a readable string not raw bytes
        ) 

        return result.stdout #result = object, stdout = standard output

    except Exception as e:
        return f"Error: {e}"# if error found dont crash, return in readable format message
    
def main():

    report = ""

    report += "=" * 50 + "\n"
    report += "SYSTEM INFORMATION REPORT\n"
    report += "=" * 50 + "\n"

    report += f"User: {get_user()}\n" #USES ALL FUNCTIONS TO CREATE A CLEAN FORMAT FOR RESULTS
    report += f"Hostname: {get_hostname()}\n"
    report += f"Date: {get_time()}\n\n"

    report += "System Information:\n"
    report += run_command(["uname", "-a"])

    report += "\nDisk Usage:\n"
    report += run_command(["df", "-h"])

    report += "\nMemory Usage:\n"
    report += run_command(["free", "-h"])

    print(report)

    with open("report.txt", "w") as file:
        file.write(report)

    print("\nReport saved to report.txt")

if __name__ == "__main__":
    main()
