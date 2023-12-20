"""Takes in URL, sends request, displays value of X-Request-Id found in header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    with requests(argv[1]) as f:
        print(f.info().get("X-Request-Id"))
        