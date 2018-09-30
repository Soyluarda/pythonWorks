from multiprocessing import Pool
from math import sqrt,floor

def asal_mi(sayi):
    "sayi asal mi?"
    if sayi < 2:
        raise ValueError("sayi ikiden buyuk olmalidir.")

    if sayi == 2:
        return True

    if sayi %2 == 0:
        return False

    bolunecekler = range(3,int(sqrt(sayi)),2)

    for b in bolunecekler:
        if sayi % b == 0:
            return False
    return True

def sayilar_asal_mi(sayilar):
    "bir liste icindeki asallari dondur"
    return [x for x in sayilar if asal_mi(x)]

if __name__ == "__main__":
    p = Pool(processes=4)

    sonuclar = p.map(sayilar_asal_mi,[range(500000,625000),
    range(625000,750000),
    range(750000,875000),
    range(875000,1000000)])

    alt_toplamlar = map(sum,sonuclar)
    print alt_toplamlar
    print sum(alt_toplamlar)
