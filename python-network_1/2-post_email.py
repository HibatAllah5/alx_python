"""Takes in URL and email, sends POST request using given parameters, displays
body of response decoded in utf-8"""
if __name__ == "__main__":
    from requests import requests
    from sys import argv

    with requests.requests(argv[1]) as f:
        print(f.info().get("X_Request_Id"))
        
