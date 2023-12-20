import requests
import sys 

if __name__ == "__main__":

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = requests(value)
    req = requests(url, data.encode('ascii'))
    with requests(req) as response:
        data = response.read()
    print("Email: test@test.com")
