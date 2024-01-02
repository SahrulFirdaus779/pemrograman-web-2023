nama = str(input("Masukkan nama anda: "))
nomor = int(input("Masukkan nomor hp anda: "))
x = int(input("Pilih 1 untuk makanan, pilih 2 untuk minuman: "))
match x:
    case 1:
        print("1. Nasi Goreng, 2. Mie Goreng, 3. Ayam Geprek")
        y = int(input("Pilih pesanan anda sesuai angka: "))
        if y == 1:
            a = int(input("Masukkan jumlah pesanan anda: "))
            print("Nama:",nama)
            print("Nomor Hp:",nomor)
            print("Nasi Goreng")
            print("Jumlah pesanan:",a)
            print("Total Harga:",a*15000)
        if y == 2:
            a = int(input("Masukkan jumlah pesanan anda: "))
            print("Nama:",nama)
            print("Nomor Hp:",nomor)
            print("Mie Goreng")
            print("Jumlah pesanan:",a)
            print("Total Harga:",a*12000)
        if y == 3:
            a = int(input("Masukkan jumlah pesanan anda: "))
            print("Nama:",nama)
            print("Nomor Hp:",nomor)
            print("ayam geprek")
            print("Jumlah pesanan:",a)
            print("Total Harga:",a*18000)
    case 2:
        print("1. Aneka Jus, 2. Soft Drink, 3. Sweet Ice Tea")
        y = int(input("Pilih pesanan anda sesuai angka: "))
        if y == 1:
            a = int(input("Masukkan jumlah pesanan anda: "))
            print("Nama:",nama)
            print("Nomor Hp:",nomor)
            print("Aneka Jus")
            print("Jumlah pesanan:",a)
            print("Total Harga:",a*15000)
        if y == 2:
            a = int(input("Masukkan jumlah pesanan anda: "))
            print("Nama:",nama)
            print("Nomor Hp:",nomor)
            print("Soft Drink")
            print("Jumlah pesanan:",a)
            print("Total Harga:",a*10000)
        if y == 3:
            a = int(input("Masukkan jumlah pesanan anda: "))
            print("Nama:",nama)
            print("Nomor Hp:",nomor)
            print("Sweet Ice Tea")
            print("Jumlah pesanan:",a)
            print("Total Harga:",a*5000)
    case _:
        print("Anda salah angka")