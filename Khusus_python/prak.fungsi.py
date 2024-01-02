'''1. buatlah fungsi untuk menampilakan data diri :
contoh pemanggilan : profil(nama, alamat, gender, umur, hoby)
'''
def profil(nama, alamat, gender, umur, hoby):
    print("Data Diri")
    print("Nama:", nama)
    print("alamat:", alamat)
    print("gender:", gender)
    print("umur:", umur,"tahun")
    print("hoby:",hoby)
profil(" sahrul firdaus","Ciawi, Bogor","laki-laki", "18", "membaca")

'''2. buatlah fungsi untuk mencari kelulusan nilai dari berikut :
jika nilai < 60 maka gagal 
jika nilai = 61 - 70 maka baik 
jika nilai = 71 - 80 maka sangat baik 
jika nilai = 81 - 100 maka istimewa'''

def cek_kelulusan(nilai):
    if nilai <= 60:
        return "Gagal"
    elif 61<= nilai <=70:
        return "Baik"
    elif 71<= nilai <=80:
        return "Sangat Baik"
    elif 81<= nilai <=100:
        return "Istimewa"
    else:
        return "Nilai tidak terdefinisi masukan angka 1-100"   
print(cek_kelulusan(int(input("Masukkan Nilai: "))))

'''3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang di masukan :
ex : ganjil (100)'''

def ganjil(batas):
    for nilai in range(1, batas+1, 2):
        print(nilai)

print(ganjil(int(input("Masukan Batas nilai:"))))
