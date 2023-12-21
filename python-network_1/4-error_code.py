import sys
import requests


if __name__ == "__main__":
    url = (" ")

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("Regular request")
