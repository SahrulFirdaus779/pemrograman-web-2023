#ini soal nomor pertama
#inputan pertama
x = str(input("Kendaraan motor atau mobil? "))
pertalite = 12
pertamax = 13
pertamaxturbo = 13.5
jakarta = 20
bekasi = 35.7
depok = 5
tangerang = 99
bogor = 120.6
y=[pertalite,pertamax,pertamaxturbo]
z=[jakarta,bekasi,depok,tangerang,bogor]
match x:
    case "MOTOR"|"Motor"|"motor"|"mobil"|"Mobil"|"MOBIL":
#inputan kedua
        y = str(input("Jenis bensin: (pertalite, Pertamax, Pertamax Turbo)? "))
match y:
    case "PERTALITE"|"pertalite"|"Pertalite"|"PERTAMAX"|"Pertamax"|"pertamax"|"pertamaxturbo"|"PertamaxTurbo"|"PERTAMAXTURBO":
#input ketiga
        z = input("Kota yang dituju: ")
match z:
    case "JAKARTA"|"jakarta"|"Jakarta":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",jakarta/pertalite,"liter")
        print("Dengan total harga bensin pertalite adalah Rp",int(jakarta/pertalite*10000))
    case "BEKASI"|"bekasi"|"Bekasi":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",bekasi/pertalite,"liter")
        print("Dengan total harga bensin pertalite adalah Rp",int(bekasi/pertalite*10000))
    case "DEPOK"|"depok"|"Depok":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",depok/pertalite,"liter")
        print("Dengan total harga bensin pertalite adalah Rp",int(depok/pertalite*10000))
    case "TANGERANG"|"Tangerang"|"tangerang":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",tangerang/pertalite,"liter")
        print("Dengan total harga bensin pertalite adalah Rp",int(tangerang/pertalite*10000))
    case "BOGOR"|"bogor"|"Bogor":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",bogor/pertalite,"liter")
        print("Dengan total harga bensin pertalite adalah Rp",int(bogor/pertalite*10000))
    case "PERTAMAX"|"Pertamax"|"pertamax":
        z = input("Kota yang dituju: ")
match z:
    case "JAKARTA"|"jakarta"|"Jakarta":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",jakarta/pertamax,"liter")
        print("Dengan total harga bensin pertamax adalah Rp",int(jakarta/pertamax*14000))
    case "BEKASI"|"bekasi"|"Bekasi":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",bekasi/pertamax,"liter")
        print("Dengan total harga bensin pertamax adalah Rp",int(bekasi/pertamax*14000))
    case "DEPOK"|"depok"|"Depok":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",depok/pertamax,"liter")
        print("Dengan total harga bensin pertamax adalah Rp",int(depok/pertamax*14000))
    case "TANGERANG"|"Tangerang"|"tangerang":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",tangerang/pertamax,"liter")
        print("Dengan total harga bensin pertamax adalah Rp",int(tangerang/pertamax*14000))
    case "BOGOR"|"bogor"|"Bogor":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",bogor/pertamax,"liter")
        print("Dengan total harga bensin pertamax adalah Rp",int(bogor/pertamax*14000))
    case "PERTAMAX TURBO"|"Pertamax Turbo"|"pertamax turbo"|"PERTAMAXTURBO"|"PertamaxTurbo"|"pertamaxturbo":
            z = input("Kota yang dituju: ")
match z:
    case "JAKARTA"|"jakarta"|"Jakarta":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",jakarta/pertamaxturbo,"liter")
        print("Dengan total harga bensin pertamax turbo adalah Rp",int(jakarta/pertamaxturbo*17000))
    case "BEKASI"|"bekasi"|"Bekasi":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",bekasi/pertamaxturbo,"liter")
        print("Dengan total harga bensin pertamax turbo adalah Rp",int(bekasi/pertamaxturbo*17000))
    case "DEPOK"|"depok"|"Depok":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",depok/pertamaxturbo,"liter")
        print("Dengan total harga bensin pertamax turbo adalah Rp",int(depok/pertamaxturbo*17000))
    case "TANGERANG"|"Tangerang"|"tangerang":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",tangerang/pertamax,"liter")
        print("Dengan total harga bensin pertamax turbo adalah Rp",int(tangerang/pertamaxturbo*17000))
    case "BOGOR"|"bogor"|"Bogor":
        print("Bensin yang dipakai dengan kendaraan",x,"ke Kota",z,"adalah",bogor/pertamax,"liter")
        print("Dengan total harga bensin pertamax turbo adalah Rp",int(bogor/pertamaxturbo*17000))
    case _:print("Silahkan pilih motor atau mobil")