print("Pilih Oprasi")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Perpangkatan")
print("6. Modulus")
print("7. pembagian bulat")
print("8. akar")
print("9. nilai sin")
print("10. nilai cos")
print("11. nilai tan")

oprasi= int(input("Masukan pilihan oprasi(1/2/3/4/5/6/7/8/9/10/11) : "))

import aritmatika
if oprasi == 1:
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan kedua: '))
    aritmatika.tambah(a,b)

elif oprasi == 2:
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan kedua: '))
    aritmatika.kurang(a,b)

elif oprasi == 3:
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan kedua: '))
    aritmatika.kali(a,b)

elif oprasi == 4:
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan kedua: '))
    aritmatika.bagi(a,b)

elif oprasi == 5:
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan kedua: '))
    aritmatika.pangkat(a,b)

elif oprasi == 6:
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan kedua: '))
    aritmatika.modulus(a,b)

elif oprasi == 7:
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan kedua: '))
    aritmatika.pembagian_bulat(a,b)

elif oprasi == 8:
    a = int(input('masukan bilangan: '))
    aritmatika.akar(a)

elif oprasi == 9:
    a = int(input('masukan nilai: '))
    aritmatika.sin(a)

elif oprasi == 10:
    a = int(input('masukan nilai: '))
    aritmatika.cos(a)

elif oprasi == 11:
    a = int(input('masukan nilai: '))
    aritmatika.tan(a)