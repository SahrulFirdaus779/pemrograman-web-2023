

#class name
class Person:
    #konstruktor
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    #return
    def makan(self):
        print("saya bisa makan mie ayam")
    def bekerja(self):
        print("saya adalah seorang programmer")
    def printname(self):
        print("Nama Saya ", self.firstname, self.lastname)
#objek
x = Person("Sahrul", "Firdaus")
x.printname()
x.makan()

#child class 4
class student(Person):
    def __init__(self, fname, lname,prodi,angkatan):
        super().__init__(fname, lname)
        self.angkatan = angkatan
        self.prodi= prodi
    def welcome(self):
        print("Hai saya", self.firstname, self.lastname, "saya dari",self.prodi, self.angkatan)

x = student("sahrul","firdaus,","Teknik Informatika", 2023)
x.welcome()
