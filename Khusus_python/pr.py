# print('''
# Buat fungsi untuk menampilkan nama2 siswa yang lulus
# saja dari hasil_akhir di slide sebelumnya (nilai > 65)
# hasil_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}
# ]
# lulus_saja(hasil_akhir) hasilnya:['Reza', 'Dian']
# ''')
def siswa_lulus(hasil_akhir):
    siswa_lulus= [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] >65]
    #siswa yang lulus adalah siswa yang nilainya lebih dari 65
    return siswa_lulus

hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]
print(siswa_lulus(hasil_akhir))

# print('''1. Buat fungsi untuk membuat list baru berisi urutan terbalik dari buah2an
# menggunakan for dan materi yang sudah diajarkan. (tidak boleh pakai
# fungsi dari python).
# balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']) hasilnya :['jambu',
# 'durian', 'pisang', 'mangga', 'pepaya']
# ''')
nama_buah=['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
print(nama_buah[::-1])

# print('''2. Buat fungsi untuk membuat list baru berisi isi list buah2an tetapi
# terduplikasi.
#     duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])''')

list_buah=[]
daftar_buah=['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
for buah in daftar_buah:
    list_buah=list_buah + [buah]*2
print(list_buah)

# print('''3. Buat fungsi untuk membuat string baru berisi hanya konsonan dari string
# fungsi(“Nurul Fikri”) Hasilnya: "NrlFkr"
# ''')
def filter_konsonan(string):
    konsonan = ""
    for huruf in string:
        if huruf.isalpha() and huruf.lower() not in 'aeiouAIUEO':
            konsonan += huruf
    return konsonan

# Contoh penggunaan
string = "Nurul Fikri"
hasil = filter_konsonan(string)
print("Hasilnya:", hasil)


