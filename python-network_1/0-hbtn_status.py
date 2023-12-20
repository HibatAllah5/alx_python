"""Fetches https://alu-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests 

    req = requests('https://alu-intranet.hbtn.io/status')
    with requests("https://alu-intranet.hbtn.io/status") as f:
        status = f.read()
        print("Body response:\n"
              "\t- type: {}\n"
              "\t- content: {}\n")
         