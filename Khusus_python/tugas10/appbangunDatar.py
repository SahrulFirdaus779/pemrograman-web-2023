print("Pilih Oprasi Menghitung Bangun Datar")
print("1. Luas Persegi")
print("2. Keliling Persegi")
print("3. Luas Persegi panjang")
print("4. keliling Persegi panjang")
print("5. Luas Segitiga")
print("6. Keliling Segitiga")
print("7. Luas Jajargenjang")
print("8. Keliling Jajargenjang")
print("9. Luas BelahKetupat")
print("10. Keliling BelahKetupat")
print("11. Luas lingkaran")
print("12. Keliling Lingkaran")
print("13. Luas Trapesium")
print("14. Keliling Trapesium")

oprasi= int(input("Masukan pilihan oprasi(1/2/3/4/5/6/7/8/9/10/11/12/13/14) : "))

import bangun_datar

if oprasi == 1:
    a = int(input('masukan sisi Persegi: '))
    luas_persegi = bangun_datar.luas_persegi(a)
    print("luas perseginya adalah", luas_persegi)

elif oprasi == 2:
    a = int(input('masukan sisi Persegi: '))
    keliling_persegi = bangun_datar.keliling_persegi(a)
    print("keliling perseginya adalah", keliling_persegi)

elif oprasi == 3:
    a = int(input('masukan sisi panjang: '))
    b = int(input('masukan sisi Lebar: '))
    luas_persegi_panjang = bangun_datar.luas_persegi_panjang(a,b)
    print("luas persegi panjang =", luas_persegi_panjang)

elif oprasi == 4:
    a = int(input('masukan sisi panjang: '))
    b = int(input('masukan sisi Lebar: '))
    keliling_persegi_panjang = bangun_datar.keliling_persegi_panjang(a,b)
    print("luas persegi panjang =", keliling_persegi_panjang)

elif oprasi == 5:
    a = int(input('masukan sisi alas: '))
    b = int(input('masukan sisi tinggi: '))
    luas_segitiga = bangun_datar.luas_segitiga(a,b)
    print("luas segitiga =", luas_segitiga)

elif oprasi == 6:
    a = int(input('masukan sisi alas: '))
    b = int(input('masukan sisi miring 1: '))
    c = int(input('masukan sisi miring 3: '))
    Keliling_segitiga = bangun_datar.keliling_segitiga(a,b,c)
    print("keliling segitiga =", Keliling_segitiga)

elif oprasi == 7:
    a = int(input('masukan sisi alas: '))
    b = int(input('masukan sisi tinggi: '))
    luas_jajar_genjang = bangun_datar.luas_jajargenjang(a,b)
    print("luas jajar genjang =", luas_jajar_genjang)

elif oprasi == 8:
    a = int(input('masukan sisi : '))
    b = int(input('masukan sisi miring: '))
    keliling_jajar_genjang = bangun_datar.keliling_jajargenjang(a,b)
    print("keliling jajar genjang =", keliling_jajar_genjang)

elif oprasi == 9:
    a = int(input('masukan diagonal pertama: '))
    b = int(input('masukan diagonal kedua: '))
    luas_belah_ketupat = bangun_datar.luas_belah_ketupat(a,b)
    print("luas belah ketupat =", luas_belah_ketupat)

elif oprasi == 10:
    a = int(input('masukan sisi diagonal: '))
    keliling_belah_ketupat = bangun_datar.keliling_belah_ketupat(a)
    print("keliling belah ketupat =", keliling_belah_ketupat)

elif oprasi == 11:
    a = int(input('masukan nilai jari jari: '))
    luas_lingkaran = bangun_datar.luas_lingkaran(a)
    print("luas kelilig =", luas_lingkaran)

elif oprasi == 12:
    a = int(input('masukan nilai jari jari: '))
    keliling_lingkaran = bangun_datar.keliling_lingkaran(a)
    print("keliling lingkaran", keliling_lingkaran)

elif oprasi == 13:
    a = int(input('masukan alas atas: '))
    b = int(input('masukan alas bawah: '))
    c = int(input('masukan tinggi: '))
    luas_trapesium = bangun_datar.luas_trapesium(a,b,c)
    print("luas trapesium =", luas_trapesium)

elif oprasi == 14:
    a = int(input('masukan alas atas: '))
    b = int(input('masukan alas bawah: '))
    c = int(input('masukan sisi miring 1: '))
    d = int(input('masukan sisi miring 2: '))
    keliling_trapesium = bangun_datar.keliling_trapesium(a,b,c,d)
    print("keliling trapesium =", keliling_trapesium)
