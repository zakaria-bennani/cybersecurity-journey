from modules.sysinfo import run_sysinfo
from modules.portscanner import run_portscan
from modules.loganalyzer import run_analyze_log
from modules.passwordchecker import run_password_check
import argparse

parser = argparse.ArgumentParser(
    description="Security Toolkit"
)

subparsers = parser.add_subparsers(
    dest="command"
)

subparsers.add_parser(
    "sysinfo"
)

subparsers.add_parser(
    "portscan"
)

subparsers.add_parser(
    "analyze-log"
)

subparsers.add_parser(
    "password-check"
)

args = parser.parse_args()

if args.command == "sysinfo":
    report = run_sysinfo()

elif args.command == "portscan":
    report = run_portscan()

elif args.command == "analyze-log":
    report = run_analyze_log()

elif args.command == "password-check":
    report = run_password_check()

with open(
    f"reports/{args.command}_report.txt",
    "w"
) as file:
    file.write(report)
