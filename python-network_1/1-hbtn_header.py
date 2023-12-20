if __name__ == '__main__':
   import requests
   import sys 

   with requests(sys.argv[1]) as response:
       content = response.getheader('X_Request_Id')

   print(content)
