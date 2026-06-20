import socket
import os  
from datetime import datetime

SERVICES = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-ALT"
}

def get_service(port):
    return SERVICES.get(
        port,
        "Unknown"
    )

def scan_port(target, port, timeout):

    print(f"Scanning port {port}")
    
    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(timeout)

        result = sock.connect_ex(
            (target, port)
        )
    
        sock.close()

        return result == 0

    except socket.timeout:
        return False

    except ConnectionRefusedError:
        return False

    except socket.gaierror:
        print("Hostname error")
        return False  

    except Exception as e:
        print(e)
        return False 

def scan_range(target, start, end, timeout, verbose):

    open_ports = []

    for port in range(start, end + 1):

        if scan_port(target, port, timeout):

            print(
                f"{port}/tcp OPEN "
                f"{get_service(port)}"
            )

            open_ports.append(port)

        elif verbose:

            print(
                f"{port}/tcp CLOSED"
            )

    return open_ports

def save_report(target, open_ports, mode):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"reports/scan_{timestamp}.txt"
    )

    with open(filename, "w") as file:

        file.write(
            "PORT SCAN REPORT\n"
        )

        file.write("=" * 40 + "\n")

        file.write(
            f"Target: {target}\n"
        )

        file.write(
            f"Mode: {mode}\n\n"
        )

        file.write(
            "Open Ports:\n"
        )

        for port in open_ports:

            file.write(
                f"{port} "
                f"{get_service(port)}\n"
            )

    print(
        f"\nReport saved to {filename}"
    )

def run_portscan():

    target = input("Target IP: ")

    start = int(input("Start port: "))
    end = int(input("End port: "))

    timeout = 1
    verbose = False

    open_ports = scan_range(
        target,
        start,
        end,
        timeout,
        verbose
    )

    save_report(
        target,
        open_ports,
        "manual"
    )

    return f"Scan complete. Open ports: {open_ports}"
