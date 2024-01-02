from gempa import Gempa

banten = Gempa("Banten", 1.2)
palu = Gempa("Palu", 6.1)
cianjur = Gempa("Cianjur", 5.6)
jayapura = Gempa("Jayapura", 3.3)
garut = Gempa("Garut", 4.0)

banten.dampak()
palu.dampak()
cianjur.dampak()
jayapura.dampak()
garut.dampak()