import requests
from colorama import Fore

def get_ip_info(ip_address):
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(Fore.CYAN + f"Made By BadDecisions642")
        print(Fore.MAGENTA + f"IP Address: {data.get('ip')}")
        print(Fore.MAGENTA + f"ISP: {data.get('org')}")
        print(Fore.MAGENTA + f"Region: {data.get('region')}")
        print(Fore.MAGENTA + f"Country: {data.get('country')}")
        print(Fore.MAGENTA + f"City: {data.get('city')}")
    else:
        print(Fore.RED + f"couldnt get info for {ip_address}")

if __name__ == "__main__":
    ip = input(Fore.MAGENTA + "Enter an IP to locate: ")
    get_ip_info(ip)