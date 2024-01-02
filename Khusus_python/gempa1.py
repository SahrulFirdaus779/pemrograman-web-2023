class Gempa:
    lokasi=''
    skala=''

    def __init__(self,lokasi,skala):
        self.lokasi= lokasi
        self.skala= skala

    def dampak(self):
        if self.skala < 2:
            print ("\n==========================",
                    "\n Gempa di\t: ", self.lokasi,
                    "\ndengan skala\t:", self.skala,
                    "\nGempa tidak berasa"
                    "\n========================="
                    )
        elif 2 <= self.skala <= 4:
            print ("\n==========================",
                    "\n Gempa di\t: ", self.lokasi,
                    "\ndengan skala\t:", self.skala,
                    "\nDampak gempa bangunan retak retak"
                    "\n========================="
                    )
        elif 4 <= self.skala <= 6:
            print ("\n==========================",
                    "\n Gempa di\t: ", self.lokasi,
                    "\ndengan skala\t:", self.skala,
                    "\nDampak gempa bangunan roboh"
                    "\n========================="
                    )
        elif self.skala >= 6:
            print ("\n==========================",
                    "\n Gempa di\t: ", self.lokasi,
                    "\ndengan skala\t:", self.skala,
                    "\nDampak gempa bangunan roboh dan berpotensi tsunami"
                    "\n========================="
                    )