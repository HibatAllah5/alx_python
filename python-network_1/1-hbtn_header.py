"""Takes in URL, sends request, displays value of X-Request-Id found in header
"""
if __name__ == "__main__":
    from urllib import requests
    from sys import argv

    with requests.urlopen(argv[1]) as f:
        print(f.info().get("X-Request-Id"))

