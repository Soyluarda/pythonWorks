import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/telefon-ve-aksesuarlari?pg=1"
r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
urunler = soup.find_all("li",attrs={'class':'column'})

for urun in urunler:
    urun_adi =(urun.a.get("title"))
    urun_link = (urun.a.get("href"))

    urun_r = requests.get(urun_link)
    urun_soup = BeautifulSoup(urun_r.content)
    ozellikler = urun_soup.find_all("section",attrs={"class":"features"})
    for ozellik in ozellikler:
        print (ozellik.find("span",attrs={"class":"label"}))
        print (ozellik.find("span",attrs={"class":"data"}))
        print("#"*10)
