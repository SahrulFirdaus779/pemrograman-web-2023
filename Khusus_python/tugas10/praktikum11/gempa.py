class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("====>Di", self.lokasi, "Dampak gempa tidak berasa", "karena skala nya hanya", self.skala)
        elif self.skala >= 2 and self.skala <= 4:
            print("====>Di", self.lokasi ,"Dampak gempa bangunan retak-retak", "karena skala mencapai", self.skala)
        elif self.skala >= 4 and self.skala <= 6:
            print("====>Di", self.lokasi ,"Dampak gempa bangunan roboh", "karena skala nya sudah mencapai", self.skala)
        else:
            print("====> DARURATTTT!!!", "Di", self.lokasi , "Dampak gempa bangunan roboh dan berpotensi tsunami", "karena skala mencapai", self.skala)