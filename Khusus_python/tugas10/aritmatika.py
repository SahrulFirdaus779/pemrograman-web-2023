#modul matematika
import math
def tambah(bil1,bil2):
    hasil=bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)
def kurang(bil1,bil2):
    hasil=bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)
def kali(bil1,bil2):
    hasil=bil1*bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)
def bagi(bil1,bil2):
    hasil=bil1/bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)
def pangkat(bil1,bil2):
    hasil= math.pow(bil1,bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)
def modulus(bil1, bil2):
    hasil= bil1%bil2
    print("hasil modulus dari",bil1,"^",bil2,"=",hasil)
def pembagian_bulat(bil1,bil2):
    hasil= bil1//bil2
    print("hasil pembagian bulat dari",bil1,"^",bil2,"=",hasil)
def akar(bil1) :
    hasil  = math.sqrt(bil1)
    print('hasil akar dari',bil1,'=',hasil)
def sin(bil1) :
    hasil  = math.sin(bil1)
    print('hasil sin dari',bil1,'=',hasil)
def cos(bil1) :
    hasil  = math.cos(bil1)
    print('hasil cos dari',bil1,'=',hasil)
def tan(bil1) :
    hasil  = math.tan(bil1)
    print('hasil tan dari',bil1,'=',hasil)