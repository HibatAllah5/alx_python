"""Takes in URL and email, sends POST request using given parameters, displays
body of response decoded in utf-8"""

from requests import requests
from sys import argv

if __name__ == "__main__":
    req = requests(argv[1])
    with requests(req) as f :
        header = f.getheader('X_Request_Id')
        print(header)
