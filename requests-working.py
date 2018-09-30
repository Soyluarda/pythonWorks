import requests
import json

url = "yoururl.com"

r = requests.get(url)
print r.status_code

r = requests.get(url,params={"kategori":"telefon"})
print r.ok

r = requests.post(url,data={"username":"arda","pass":"1234"})
print r.status_code

r = requests.post(url,headers={"User-Agent":"Soyluarda modified"})

r = requests.post(url,headers={"Referer":"previoussite.com"})
