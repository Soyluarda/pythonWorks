from threading import Thread
from Queue import Queue
from urllib import urlopen
from time import time
from BeautifulSoup import BeautifulSoup

siteler = ("http://www.istihza.com")

ilk_sira = Queue()
ikinci_sira = Queue()

def siteokuyan():
    while True:
        site = ilk_sira.get()
        f = urlopen(site)
        icerik = f.read()
        f.close()
        ikinci_sira.put(icerik)
        ilk_sira.task_done()

def linkokuyan():
    while True:
        icerik = ikinci_sira.get()
        soup = BeautifulSoup(icerik)
        for link in soup.findAll(['a']):
            print link
        ikinci_sira.task_done()


if __name__ == "__main__":
    basla = time()
    for i in range(5):
        t = Thread(target = siteokuyan)
        t.daemon = True
        t.start()

    for site in siteler:
        ilk_sira.put(site)

    for i in range(5):
        t = Thread(target = linkokuyan)
        t.daemon = True
        t.start()

    ilk_sira.join()
    ikinci_sira.join()

    print "%f saniye " %(time() - basla)
