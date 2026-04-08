import requests

url='https://news.163.com'
print(requests.get(url).text)