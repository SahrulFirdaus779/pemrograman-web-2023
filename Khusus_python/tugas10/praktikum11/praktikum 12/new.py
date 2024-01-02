class Person:
    nama = ""
    gender = ""
    umur = 0
    def __init__(self,nama,gender,umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur
    def cetak(self):
        print("Nama \t\t :",self.nama,
            "\nJenis Kelamin \t :",self.gender,
            "\nUmur \t\t :",self.umur)
        
class Dosen(Person):
    #pass jika tidak ada tambahan property dan method lainnya
    gelar =""
    jabatan=""
    gaji= 0
    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
        
    def setGaji(self,uang):
        self.gaji += uang
    def cetak(self):
        super().cetak()
        print("Gelar \t\t :",self.gender,
            "\nJabatan \t :",self.jabatan,
            "\nGaji \t\t : Rp.",self.gaji,
            "\n-------------------------------")

class Mahasiswa(Person):
    prodi=""
    semester=0
    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama, gender, umur)
        self.prodi=prodi
        self.semester=semester
    def cetak(self):
        super().cetak()
        print("Prodi \t\t :",self.prodi,
            "\nSemester \t :",self.semester,
            "\n-------------------------------")
        
#ciptakan object
m1= Mahasiswa('Siti Aminah','Wanita',20,'SI',3)
m2= Mahasiswa('Budi Santoso','Pria',23,'TI',5)
d1= Dosen('Sirojul Munir','Pria',43,'S.Si, M.Kom', 'LPPM')
d2= Dosen('Henry Saptono','Pria',44,'S.Si, M.Kom', 'LTSI')#gunakan fungsi2 yg ada di class 
d1.setGaji(12000000)
d2.setGaji(10000000)
m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()


        

