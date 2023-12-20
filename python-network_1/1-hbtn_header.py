import requests
import sys 

url=  "https://alu-intranet.hbtn.io/status"

request_headers = {'X-Request-Id'}

response= requests.get(url=url, headers= request_headers)

print(response.headers)
