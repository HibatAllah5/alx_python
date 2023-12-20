"""Fetches holberton/ statue page"""
import requests

if __name__ == "__main__":
    r = requests.get("https://alu-intranet.hbtn.io/status")
    with (r) as response:
        data = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
