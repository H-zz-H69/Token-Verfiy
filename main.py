import os
import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

def logo():
    print(f"""{Fore.MAGENTA}
       ==----------     ---------:      
       =-:-:::::--:     -::::::--:      
       --:+     -::     -:     =-:      
      +=-:=     -::     ::     =-:=     
      ::::::::::::::::::::     =-:+     
      ::                       =-:=     
      ::                       =-:=     
      ::--=====================--:---   
       --:-                       -::   
       =-:+                       -::   
       =-:+                       -:-   
       =-:+     -::-----------::::::-   
       =-:+     -::     ::     =-:=     
       =-:+     -::     ::     =-:=     
       =-:+     -:-     ::     =-:      
       =-:+     -::     ::     --:      
       =-:=++===-:-     ::-====--:      
       --::::::::::     ::::::::::    {Fore.LIGHTMAGENTA_EX}
       https://github.com/H-zz-H69
              Made by H-zz-H  
    """)

def verify_token(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": token}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 429:
        retry_after = response.json().get("retry_after", 1)
        print(f"{Fore.YELLOW}Rate limited. Warte {retry_after} Sekunden...")
        time.sleep(retry_after)
        return verify_token(token)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "token": token,
            "username": data.get("username", "Unknown"),
            "email": data.get("email", "Unknown"),
            "phone": data.get("phone", "Not available"),
            "nitro": "Yes" if data.get("premium_type", 0) > 0 else "No"
        }
    return None

def update_title(found, verified):
    os.system(f'title H-zz-H ^| Found: {found} ^| Verified: {verified}')

def main():
    logo()
    folder = "Other"
    output_file = "verified_tokens.txt"
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"{Fore.GREEN}Ordner 'Other' got created.")
        return
    
    token_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    all_tokens = []
    for file in token_files:
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            all_tokens.extend(f.read().splitlines())
    
    found = 0
    verified = 0
    verified_tokens = []
    verified_info = []
    nitro_users = []
    
    for token in all_tokens:
        found += 1
        token_data = verify_token(token)
        if token_data:
            verified += 1
            verified_tokens.append(token_data["token"])
            verified_info.append(token_data)
            print(f"{Fore.GREEN}Checked Tokens: {found}/{len(all_tokens)} # Checked")
            if token_data["nitro"] == "Yes":
                nitro_users.append(f"{token_data['username']} ({token_data['email']})\n{token_data['token']}")
        else:
            print(f"{Fore.CYAN}Checked Tokens: {found}/{len(all_tokens)}")
        update_title(found, verified)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(verified_tokens))
    
    print(f"{Fore.GREEN}\nFinished. Found tokens: {found}, Verified Tokens: {verified}\n")
    
    if verified_info:
        print(f"{Fore.LIGHTCYAN_EX}Verified Token Information:")
        for info in verified_info:
            print(f"{Fore.GREEN}Token: {info['token']}\n{Fore.CYAN}Username: {info['username']}\nEmail: {info['email']}\nPhone: {info['phone']}\nNitro: {info['nitro']}\n")
    
    if nitro_users:
        print(f"{Fore.MAGENTA}\nAccounts with Nitro:")
        for user in nitro_users:
            print(f"{Fore.YELLOW}- {user}\n")

if __name__ == "__main__":
    main()
