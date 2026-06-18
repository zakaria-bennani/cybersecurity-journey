import socket
import argparse
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

    except Exception as e:
        print(e)

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

def main():
    parser = argparse.ArgumentParser(
        description="Port Scanner"
    )

    parser.add_argument(
        "--target",
        required=True
    )

    parser.add_argument(
        "--start",
        type=int,
        required=True
    )

    parser.add_argument(
        "--end",
        type=int,
        required=True
    )

    parser.add_argument(
        "--mode",
        choices=[
            "fast",
            "thorough"
        ],
        default="fast"
    )

    parser.add_argument(
        "--verbose",
        action="store_true"
    )

    args = parser.parse_args()

    if args.mode == "fast":
        timeout = 0.3

    else:
        timeout = 1

    try:

        open_ports = scan_range(
            args.target,
            args.start,
            args.end,
            timeout,
            args.verbose
        )

        save_report(
            args.target,
            open_ports,
            args.mode
        )

    except KeyboardInterrupt:

        print(
            "\nScan interrupted by user."
        )

if __name__ == "__main__":
    main()