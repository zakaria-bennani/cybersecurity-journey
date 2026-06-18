# Python Port Scanner

## Overview

This project is a TCP port scanner written in Python using the built-in `socket` library.

The scanner attempts to establish TCP connections to ports on a target system and reports which ports are open. Results can be displayed in the terminal and saved to a timestamped report file.

This project was built as part of my cybersecurity learning journey to better understand networking, TCP connections, sockets, and security reconnaissance techniques.

---

## Features

- Scan a user-specified target
- Scan custom port ranges
- TCP socket-based scanning
- Service name identification for common ports
- Fast and thorough scan modes
- Verbose mode for displaying closed ports
- Timestamped report generation
- Graceful error handling
- Keyboard interrupt handling (CTRL+C)

---

## Technologies Used

- Python 3
- socket
- argparse
- datetime

No third-party libraries are required.

---

## How Port Scanning Works

A port scanner attempts to connect to ports on a target host.

If a connection succeeds:

```text
Port is OPEN
```

If a connection fails:

```text
Port is CLOSED
```

This helps security professionals identify services exposed to a network.

Example:

```text
22/tcp OPEN SSH
80/tcp OPEN HTTP
443/tcp OPEN HTTPS
```

---

## Usage

Scan ports 1–1024:

```bash
python3 scanner.py --target 127.0.0.1 --start 1 --end 1024
```

Fast scan:

```bash
python3 scanner.py --target 127.0.0.1 --start 1 --end 1024 --mode fast
```

Thorough scan:

```bash
python3 scanner.py --target 127.0.0.1 --start 1 --end 1024 --mode thorough
```

Verbose mode:

```bash
python3 scanner.py --target 127.0.0.1 --start 1 --end 100 --verbose
```

---

## Example Output

```text
22/tcp OPEN SSH
80/tcp OPEN HTTP
443/tcp OPEN HTTPS
```

Report generated:

```text
reports/scan_20260618_163945.txt
```

---

## Security Relevance

Port scanning is commonly used for:

- Network reconnaissance
- Asset discovery
- Security assessments
- Attack surface analysis
- Vulnerability management

Security engineers use port scanning to identify services that may require monitoring, hardening, or patching.

---

## Ethical Use

This tool is intended for educational purposes and authorized security testing only.

Only scan:

- Systems you own
- Lab environments
- Systems where you have explicit permission

Unauthorized scanning may violate laws, regulations, or organizational policies.

---

## Lessons Learned

Through this project I learned:

- Python sockets
- TCP connections
- Error handling
- Command-line interfaces with argparse
- Report generation
- Basic security automation

---

## Future Improvements

- Multi-threaded scanning
- UDP scanning
- Banner grabbing
- Service version detection
- Export results to CSV
- Host discovery

## Screenshot

<img width="920" height="1032" alt="image" src="https://github.com/user-attachments/assets/2c478e33-56b8-47d4-8e74-a50be9a7147b" />

