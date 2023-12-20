"""Fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    from urllib import requests

    with requests.urlopen("https://intranet.hbtn.io/status") as f:
        status = f.read()
        print("Body response:\n"
              "\t- type: {}\n"
              "\t- content: {}\n"
              "\t- utf8 content: {}".format(type(status), status,
                                            status.decode("utf-8")))
        
        