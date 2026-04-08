import requests
req = requests.get('http://docs.python-requests.org/en/master/')
print(type(req))
print(req.status_code)
print(req.encoding)
print(req.cookies) 