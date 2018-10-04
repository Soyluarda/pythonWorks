import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

r = requests.get(url)
#print r.json()
print ("#"*20)
print r.json()['bpi']['USD']['rate']
