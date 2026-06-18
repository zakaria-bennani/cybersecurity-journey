import socket
import argparse

def scan_port(target, port):
    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(1)

        result = sock.connect_ex(
            (target, port)
            )
    
        sock.close()

        return result == 0
    
    except socket.timeout:
        return False

    except socket.error:
        return False

print(
    scan_port(
        "127.0.0.1",
        22
    )
)

def scan_range(
        target,
        start,
        end):
    
    open_ports = []

    for port in range(
        start,
        end + 1):

        if scan_port(target, port):

            open_ports.append(
                port
            )

    return open_ports

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

args = parser.parse_args()