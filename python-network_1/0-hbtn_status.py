import requests

url = "https://alu-intranet.hbtn.io/status"

requests.get(url)
             
print("Body response:\n"
      "\t- type: {}\n"
      "\t- content: {}\n")
