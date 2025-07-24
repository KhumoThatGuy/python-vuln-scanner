import json

def save_report(vulnerabilities, filename="vulnerability_report.json"):
    with open(filename, 'w') as report_file:
        json.dump(vulnerabilities, report_file, indent=4)
    print(f"[+] Report saved to {filename}")
