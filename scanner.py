def run_nmap_scan(target):
    print(f"[+] Scanning target {target} with Nmap...")
    try:
        # Run Nmap scan with version detection and save output as XML
        result = subprocess.check_output(
            ['nmap', '-sV', '-T4', '-oX', 'scan_results.xml', target],
            stderr=subprocess.STDOUT
        )
        print("[+] Scan complete, results saved as scan_results.xml.")
        return 'scan_results.xml'
    except subprocess.CalledProcessError as e:
        print(f"[-] Nmap scan failed: {e.output.decode()}")
        return None
