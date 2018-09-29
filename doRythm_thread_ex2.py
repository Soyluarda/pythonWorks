from time import sleep
from threading import Thread

def Rythmbox(yaz,bekle):
    while True:
        print yaz
        sleep(bekle)

if __name__ == "__main__":
    dum = Thread(target = Rythmbox,args=("dum",1))
    cis = Thread(target = Rythmbox,args=("cis",1.5))
    tak = Thread(target = Rythmbox,args=("tak",2))

    dum.start()
    cis.start()
    tak.start()
