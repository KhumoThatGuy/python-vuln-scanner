# 🔍 Python Vulnerability Scanner

A beginner-friendly network vulnerability scanner built in Python using:

- 🛠️ Nmap (for port & service scanning)
- 🔐 Vulners API (for finding CVEs)
- 🌐 Shodan API (for OSINT and public data)
- 🧾 JSON report output

## 🧰 Features
- Scans a target IP for open ports and services
- Automatically checks for known vulnerabilities (CVEs)
- Retrieves extra info from Shodan
- Outputs a JSON report with all results

## 🚀 How to Use

```bash
python3 main.py <target-ip>
