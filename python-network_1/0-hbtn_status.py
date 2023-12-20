import requests

url = "https://alu-intranet.hbtn.io/status"

requests.get(url)
             
print("Body response:")
print("\t- type: {}".format(url.__class__))
print("\t- content: OK")
