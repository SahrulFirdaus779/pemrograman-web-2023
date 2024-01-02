#membuat function & memanggil function
#deklarasi fungsi:
def fungsi_pertambahan(a,b):
    print(a+b)
#memanggil Fungsi :
fungsi_pertambahan(4,7)
#argumen
def nama_fungsi(nama ) :
	print("ahmad "+ nama)
nama_fungsi("maulana")
nama_fungsi("bihaqi")
#argumen harapannya 2
def my_function(namaDepan, namaBelakang):
    print(namaDepan +" "+ namaBelakang)
my_function("ahmad", "Baihaqi")
#argumen kalo banyak
def my_function(*nama):
    print("nama singkat saya adalah "+ nama[0])
    #ngitungnya dari nol ya kawan
my_function("ahmad", "Baihaqi","Toha")
#nilai parameter default
def my_function(nama = "ahmad"):
    print(" nama saya adalah "+nama)
my_function("Baihaqi",)
my_function("toha")
my_function( )
#Function with return(ntuk membiarkan fungsi mengembalikan nilai)
def my_function(x):
    return x*2
print(my_function(8))
print(my_function(2))
print(my_function(9))

#bisa juga kita buat inputan

def Luaspersegi(sisi):
    luas= sisi*sisi
    return luas

print(Luaspersegi(int(input("masukan angka"))))


