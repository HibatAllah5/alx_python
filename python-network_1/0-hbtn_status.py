"""Fetches holberton/ statue page"""

if __name__ == "__main__":
    import requests 

    
    with requests("https://alu-intranet.hbtn.io/status") as response:
        status = response.read()
        print("Body response:\n"
              "\t- type: {}\n"
              "\t- content: {}\n")
