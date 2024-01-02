#modulu matematika dengan import

import matematika

hasil_tambah= matematika.tambah(1,2,3,4,5)
print(f"hasil tambah ={hasil_tambah}")

hasil_kali= matematika.kali(1,2,3,4,5)
print(f"hasil kali ={hasil_kali}")

pangkat_3= matematika.pangkat(3)
print(f"hasil pangkat ={pangkat_3(3)}")
print(" ")
#pake from

from matematika import tambah, kali, pangkat

hasil_tambah= tambah(1,2,3,4,5)
print(f"hasil tambah ={hasil_tambah}")

hasil_kali= kali(1,2,3,4,5)
print(f"hasil kali ={hasil_kali}")

pangkat_3= pangkat(3)
print(f"hasil pangkat ={pangkat_3(3)}")
print(" ")
#pake alias

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as p

hasil_tambah= add(1,2,3,4,5)
print(f"hasil tambah ={hasil_tambah}")

hasil_kali= k(1,2,3,4,5)
print(f"hasil kali ={hasil_kali}")

pangkat_3= p (3)
print(f"hasil pangkat ={pangkat_3(3)}")


import math

hasil = math.tambah (1,5)
print("hasil_tambah_dari",1,"+",5,"=",hasil)
