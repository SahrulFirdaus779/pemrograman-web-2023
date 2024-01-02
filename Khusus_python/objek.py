'''
Class dan Object
Python adalah bahasa pemrograman
berorientasi objek.
Hampir semua yang ada di Python adalah
objek, dengan properti dan methodnya.
Class seperti konstruktor objek, atau “Blue
Print" untuk membuat objek.
Membuat Class dan Objek
Class
Buat kelas bernama MyClass, dengan properti bernama x:
class MyClass:
x = 5
Objek
Sekarang kita bisa menggunakan kelas bernama MyClass untuk
membuat objek:
Contoh
Buat objek bernama p1, dan cetak nilai x:
p1 = MyClass()
print(p1.x)
'''
#class
class MyClass:
    x = 5
#objek
p1=MyClass()
print(p1.x)
print(" ")
class person:
    def __init__(self,name, age):
        self.name= name
        self.age=age
#objek
p2= person("sahrul",19)

print(p2.name)
print(p2.age)