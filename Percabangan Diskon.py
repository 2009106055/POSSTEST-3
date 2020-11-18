print("-$ ========================== $-")
print("-$ PROGRAM DISKON BY ALFAREZY $-")
print("-$ ========================== $-")
print("")
print("Nana Pergi Jalan Untuk Membeli takoyaki. \nSampai disana,tertulis harga setiap isi takoyaki")
print("")
print("-$=======  MENU TAKOYAKI DAISUKI   ========$-")
print("-$=======       1.Isi Udang        ========$-")
print("-$========      2.Isi Cumi         ========$-")
print("-$======== Silahkan Dipilih ya :)  ========$-")
print("")

Varian1 = int(input("Berapa Takoyaki Isi Udang Yang Ingin Di beli: "))
harga_takoyakiVarian1 = int(input("Masukkan Total Harga Yang sudah di hitung: "))

if harga_takoyakiVarian1 == 2000 or Varian1 >= 8:
    diskon = harga_takoyakiVarian1*8/100
    bayar = harga_takoyakiVarian1-diskon
    print("")
    print("selamat anda mendapatkan diskon 8%")
else:
    bayar = harga_takoyakiVarian1
    print("")
    print("Maaf anda tidak mendapatkan diskon karena tidak memenuhi persyaratan pembelian")

print("")
print("Harga_total:Rp. ",bayar)
print("")

Varian2 = int(input("Berapa Takoyaki Isi Cumi Yang Ingin Dibeli: "))
harga_takoyakiVarian2 = int(input("Masukkan Total Harga Yang Sudah Dihitung: "))

if harga_takoyakiVarian2 == 2500 or Varian2 >=10:
    diskon = harga_takoyakiVarian2*10/100
    bayar = harga_takoyakiVarian2-diskon
    print("")
    print("Selamat anda mendapatkan diskon 10%")
else:
    bayar = harga_takoyakiVarian2
    print("")
    print("Maaf anda tidak mendapatkan diskon karena tidak memenuhi persyaratan pembelian")

print("")
print("Harga_total:Rp. ",bayar)
print("")
print("PROGRAM END")