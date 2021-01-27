import requests
# Write your code here
url = 'https://jsonmock.hackerrank.com/api/articles?author='+'epaga'
resp = requests.get(url)
for i in resp.json()['data']:
    print(i['title'])
