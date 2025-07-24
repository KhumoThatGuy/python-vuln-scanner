import argparse
from scanner import run_nmap_scan
from vulners_api import check_vulnerabilities
from shodan_api import get_shodan_info
from report import save_report

# Function to parse Nmap XML and extract services/versions
def parse_nmap_xml(xml_file):
    import xml.etree.ElementTree as ET
    tree = ET.parse(xml_file)
    root = tree.getroot()

    services = []
    for host in root.findall("host"):
        for service in host.findall(".//service"):
            service_name = service.get("name")
            service_version = service.get("version")
            if service_name and service_version:
                services.append((service_name, service_version))
    
    return services

def main():
    parser = argparse.ArgumentParser(description="Simple Vulnerability Scanner")
    parser.add_argument("target", help="Target IP or domain to scan")
    args = parser.parse_args()

    # Run Nmap scan and parse results
    xml_file = run_nmap_scan(args.target)
    if not xml_file:
        return

    services = parse_nmap_xml(xml_file)

    all_vulnerabilities = {}

    # For each service, check for vulnerabilities
    for service, version in services:
        print(f"[+] Checking vulnerabilities for {service} {version}")
        vulnerabilities = check_vulnerabilities(service, version)
        if vulnerabilities:
            all_vulnerabilities[f"{service} {version}"] = vulnerabilities

    # Get Shodan information
    print(f"[+] Gathering Shodan info for {args.target}...")
    shodan_info = get_shodan_info(args.target)
    if shodan_info:
        all_vulnerabilities['Shodan Info'] = shodan_info
    
    # Save the results to a report
    save_report(all_vulnerabilities)

if __name__ == "__main__":
    main()
