# Buatlah kalkulator sederhana Menggunakan 4 pilihan oprasi (tambah, bagi, kali dan pengurangan)

print("================")
print("Kalkulator sederhana")
print("================")

print("powered:")
print("sahrul firdaus_0110223114")
print("")
print("Pilih Oprasi")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Pembagian")
print("4. Perkalian")

oprasi= int(input("Masukan pilihan oprasi(1/2/3/4) : "))

if oprasi == 1:
    x= int (input("Masukkan Nilai Pertama: "))
    y= int (input("Masukkan Nilai Kedua: "))
    z= x+y
    print("Hasilnya adalah:", x,"+", y, "=",z)
    print("============================")


elif oprasi == 2:
    x= int (input("Masukkan Nilai Pertama: "))
    y= int (input("Masukkan Nilai Kedua: "))
    z= x-y
    print("Hasilnya adalah:", x,"-", y, "=",z)
    print("============================")

elif oprasi == 3:
    x= float (input("Masukkan Nilai Pertama: "))
    y= float (input("Masukkan Nilai Kedua: "))
    z= x/y
    print("Hasilnya adalah:", x,"/", y, "=",z)
    print("============================")

elif oprasi == 4:
    x= int (input("Masukkan Nilai Pertama: "))
    y= int (input("Masukkan Nilai Kedua: "))
    z= x*y
    print("Hasilnya adalah:", x,"x", y, "=",z)
    print("============================")
    