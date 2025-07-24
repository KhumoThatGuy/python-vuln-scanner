import subprocess
import os

def run_nmap_scan(target):
    try:
        print(f"[+] Scanning target {target} with Nmap...")
        result = subprocess.check_output(
            ["nmap", "-sV", "-oX", "nmap_output.xml", target],
            stderr=subprocess.STDOUT,
            text=True
        )
        print("[+] Scan complete. Output saved to nmap_output.xml")
        return "nmap_output.xml"
    except subprocess.CalledProcessError as e:
        print(f"[-] Nmap scan failed: {e.output}")
        return None

