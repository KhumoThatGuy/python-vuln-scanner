import requests

def check_vulnerabilities(service, version):
    query = f"{service} {version}"
    url = f"https://vulners.com/api/v3/search/lucene/"
    params = {"query": query, "size": 5}  # Limit to top 5 CVEs
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error if the API call fails
        data = response.json()
        if data['data']['total'] > 0:
            print(f"[+] Found {data['data']['total']} vulnerabilities for {service} {version}")
            return data['data']['documents']
        else:
            print(f"[+] No vulnerabilities found for {service} {version}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"[-] API Request failed: {e}")
        return []
