# Modul Bangun Datar

def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(alas, sisi_miring1, sisi_miring2):
    return alas + sisi_miring1 + sisi_miring2

def luas_jajargenjang(alas, tinggi):
    return alas * tinggi

def keliling_jajargenjang(alas, sisi_miring):
    return 2 * (alas + sisi_miring)

def luas_belah_ketupat(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def keliling_belah_ketupat(sisi):
    return 4 * sisi

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari ** 2

def keliling_lingkaran(jari_jari):
    return 2 * 3,14 * jari_jari

def keliling_trapesium(alas1, alas2, sisi1, sisi2):
    return alas1 + alas2 + sisi1 + sisi2

def luas_trapesium(alas_atas, alas_bawah, tinggi):
    return 0.5 * (alas_atas + alas_bawah) * tinggi