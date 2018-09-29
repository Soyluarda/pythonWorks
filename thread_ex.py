from threading import Thread
from random import randint
from time import sleep

def basvuru(basvuru_id):
    sleep(randint(0,15))
    if randint(0,1):
        print "%i basvurusu kabul edildi" % basvuru_id
    else:
        print "%i basvurusu reddedildi." % basvuru_id

for i in range(5):
    Thread(target=basvuru, args=(i,)).start()
