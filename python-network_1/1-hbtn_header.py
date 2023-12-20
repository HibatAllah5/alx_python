"""Takes in URL, sends request, displays value of X-Request-Id found in header
"""
import requests
from sys import argv

url = "https://alu-intranet.hbtn.io/status"

request_headers = {"X-Request-Id"}

response = requests.get(request_headers)

print(response.headers)
