#class Name
class animal:
    nama =""
    makanan=""
    hidup=""
    berkembangbiak=""

    #konstruktor
    def __init__(self, nama,makanan,hidup,berkembangbiak):
        self.nama= nama
        self.makanan= makanan
        self.hidup= hidup
        self.berkembangbiak=berkembangbiak
    #return
    def cetak(self):
        print("-----------------------------------------"
        "\n\t Identifikasi Hewan"
        "\n-----------------------------------------"
        "\nNama Hewan\t :",self.nama,
        "\nJenis Makanan \t :",self.makanan,
        "\nHabitat Hidup \t :",self.hidup,
        "\nBerkembang biak\t :",self.berkembangbiak)

class ayam(animal):
    #tambahan properti dan method
    jenis_hewan=""
    alat_gerak=""
    def __init__(self, nama, makanan, hidup, berkembangbiak,jenis_hewan,alat_gerak):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.jenis_hewan= jenis_hewan
        self.alat_gerak= alat_gerak
    def cetak(self):
        super().cetak()
        print("Jenis Hewan\t :",self.jenis_hewan,
            "\nBergerak \t :",self.alat_gerak,
            "\n-----------------------------------------")
        
class kucing(animal):
    suara=""
    warna_bulu=""
    def __init__(self, nama, makanan, hidup, berkembangbiak, suara, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.suara= suara
        self.warna_bulu=warna_bulu
    def cetak(self):
        super().cetak()
        print("suara\t\t :", self.suara, 
        "\nWarna Bulu\t :", self.warna_bulu,
        "\n-----------------------------------------")
class ular(animal):
    bergerak=""
    warna=""
    def __init__(self, nama, makanan, hidup, berkembangbiak, bergerak, warna):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.bergerak=bergerak
        self.warna=warna
    def cetak(self):
        super().cetak()
        print("bergerak\t : ", self.bergerak, 
        "\nWarna\t\t :", self.warna,
        "\n-----------------------------------------")

#Ciptakan object
hewan1= kucing("Kucing", "Ikan", "kawasan rumah", "vivivar", "Meeonggg", "Hitam, putih, jingga")
hewan2= ayam("ayam", "Dedak", "Kawasan pertanian", "ovivar","Unggas"," dengan kedua kaki")
hewan3= ular("ular","Tikus", "Persawahan", "ovovivivar", "merayap","umumnya coklat")
hewan1.cetak()
hewan2.cetak()
hewan3.cetak()