"""Fetches https://alu-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests 
    req = requests.Request('https://alu-intranet.hbtn.io/status')
    with requests(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(html.__class__))
        print("\t- content: {}".format(html)) 
