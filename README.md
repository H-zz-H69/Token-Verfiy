# Discord Token Verifier 🔥

A simple Python tool that verifies Discord tokens from files, checks for accounts with Nitro, and outputs verified tokens to a text file.

## Features
- ✅ Verifies Discord tokens from files.
- 💾 Outputs information such as username, email, and Nitro status.
- 🚫 Handles rate-limiting by Discord’s API.
- 📄 Outputs verified tokens into a separate file (`verified_tokens.txt`).
- ⏱️ Displays live status in the terminal.

## Requirements
- Python 3.x
- `requests` library
- `colorama` library

Install the required dependencies with:

    pip install requests colorama

## Usage

1. Clone the repository:
   
    ```git clone https://github.com/H-zz-H69/Token-Verify```

3. Run the script:
   
    ```python token_verifier.py```

The script will:
- Automatically verify each token. 🔎
- Save the verified tokens in `verified_tokens.txt`. 💾
- Output detailed information for each valid token, including Nitro status. 💻
- Display any accounts that have Nitro. 🚀

## Example Output

    Ordner 'Other' got created.
    Checked Tokens: 1/10
    Checked Tokens: 2/10 # Checked
    ...
    Finished. Found tokens: 10, Verified Tokens: 4

    Verified Token Information:
    Token: xxxxxxxx
    Username: ExampleUser
    Email: example@domain.com
    Phone: Not available
    Nitro: No

## Disclaimer ⚠️
This tool is intended for educational purposes only. Misuse of this tool is strictly prohibited. 💀
