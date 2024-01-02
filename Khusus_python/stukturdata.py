'''Struktur Data
● Data dasar yang tersedia (bilangan, tulisan, logika) sering tidak
cukup
● Harus bekerja dengan data yang lebih kompleks
● Struktur data:
– Array
– List
– Stack
– Queue
– Set
– Dictionary (Map)'''

'''
Array
● Berisi sekumpulan data dengan urutan tertentu, bisa ada
duplikasi
● Diakses dengan indeks
● List di python merupakan implementasi dari array
nilai = [65, 60, 75, 0, 98]
nilai[0] == 65 # True
nilai[len(nilai)-1] == 98 # berarti indeks terakhir
len---> itu banyak jumlah nilainya'''

nilai = [65, 60, 75, 0, 98]
nilai[0] == 65 # True
nilai[len(nilai)-1] == 98

'''
Stack
● Last In First Out. Memiliki 2 operasi:
– push untuk menyimpan data ke “atas” tumpukan
– pop untuk mengambil data yang paling “atas”

list di python juga mendukung operasi stack
– append untuk push
– pop
bilangan = [1,2,3]
a = bilangan.pop()
bilangan.append(6)
print(bilangan) # => [1,2,6]
print(a) # => 3

kegunaan
● Pengecekan tanda kurung
– (a+b) * (c[d + e)
● Pencatatan undo dan redo
'''
#appand untuk masukin data baru
hasil= [65, 60, 75, 0, 98]
hasil.append(80)
print(hasil)
#pop untuk hapus data terakhir
bilangan= [65, 60, 75, 0, 98]
bilangan.pop()
print(bilangan)
'''
Queue
● Artinya “antrian”
● Struktur data FIFO (pertama dimasukkan pertama diambil)
● 2 perintah:
– enqueue (memasukkan ke antrian)
– dequeue (mengambil dari antrian)

Python list juga bisa dipakai untuk queue
bilangan = [1,2,3]
bilangan.append(6)
a=bilangan.pop(0) # Pop dengan parameter posisi
print(bilangan) # 2,3,6
print(a) # => 1
● Pakai deque (double ended queue) kinerjanya lebih bagus
(https://www.geeksforgeeks.org/queue-in-python/)

kegunaan
● Membuat sistem antrian
– Buffer di keyboard
– Mail/SMS queue (harus mengirim banyak email
sedangkan server pengirim terbatas kemampuannya)
'''

'''
Set
● Set berarti himpunan
● Tidak ada duplikasi, tidak ada jaminan urutan
● Di Python dituliskan dengan dikurung oleh kurung kurawal
{ }
a = {6, 5, 4}
print(a)

Set
● Menambahkan dengan add
● Menghapus dengan remove
● Mengambil elemen terakhir dengan pop tapi tidak ada jaminan
elemen mana yang diambil
a.add(3)
a.add(6)
a.remove(5)
print(a)
print(a.pop())
print(a)

Set
● Menggabungkan dengan union
set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)
● Memasukkan dengan update
set1 = {1,2,3}
set2 = {2,4,6}
set1.update(set2)
print(set1)
'''

'''
Dictionary
● Untuk menyimpan data yang diakses bukan dengan indeks
● Data disimpan sebagai pasangan dari key dan value
● Dituliskan dengan diapit kurung kurawal { } dan dipisah dengan
titik dua'''
data_diri = {
"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
print(data_diri["nama"])

'''
Mengakses dengan key, cth:
x = data_diri['nama'] # bisa juga data_diri.get('nama')

● Mengubah value'''
data_diri = {
"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
data_diri['nama']="Dian"
print(data_diri["nama"])

'''
● Menambah entri
data_diri['alamat'] = "Jakarta"
'''
data_diri = {
"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
data_diri['alamat']="Jakarta"
print(data_diri)

'''
● Menghapus key
data_diri.pop('alamat')'''
data_diri = {
"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
data_diri.pop('matpel')
print(data_diri)
'''
● Mengecek keberadaan key, pakai operator in
if('nama' in data_diri):
print('nama ada di data_diri')'''

data_diri = {
"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
data_diri['alamat']="Jakarta"
if('nama' in data_diri):
    print('nama ada di data_diri')

'''
list
Berisi sekumpulan data dengan urutan tertentu, bisa ada duplikasi
● Array bisa merupakan implementasi dari list
● Implementasi lain : LinkedList
– Tidak bisa diakses dengan indeks
– Memiliki akses ke entri pertama (biasanya “head”)
– Tiap entri memiliki nilai (value) dan link ke entri berikutnya (next)
daftar.head.value == 12
daftar.head.next.next.value == 37
daftar.head.next.next.next == null
'''
'''
Linked List
● Jika perlu menambahkan entri di awal
node = Node(45)
node.next = daftar.head
daftar.nead = node
● Jika perlu menambahkan entri sesudah 12
node = Node(56)
tmp = daftar.head # kita mulai dari awal
while tmp.value != 12 : # jalan sampai node 12
tmp = tmp.next
old_next = tmp.next # simpan dulu node sesudah 12 (99 dan 37)
tmp.next = node # sambungkan 56 ke sesudah 12
node.next = old_next # sambungkan 99( dan 37) ke sesudah 56'''

'''
stuktur data bertingkat
Bisa ada list di dalam list, dict di dalam list, dan sebagainya.
● Cth:
data_diri = {'nama':'Reza', 'nilai':[70, 65, 50, 85]}
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]'''
data_diri = {'nama':'Reza', 'nilai':[70, 65, 50, 85]}
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]
keluarga={"cemara":"joko", 'anaknya':['ani','ina','inz']}
print(keluarga)
print(hasil_akhir[1]['nilai'])

#new
nama_buah=['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
print(nama_buah[4])
print(nama_buah[-1])
print(nama_buah[1:3])
print(nama_buah[:3])
print(nama_buah[0:5:2])
print(nama_buah[::-1])
