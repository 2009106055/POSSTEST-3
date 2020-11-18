print("-$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$-")
print("-$$$$ WELCOME TO LOOPING PROGRAM $$$$-")
print("-$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$-")
print("")

n = int(input("Masukkan Nilai Yang Ingin Dihitung: "))
x = 0
while (x < n) :
    if (10 ** x > n):
        break
    else:
        print("kita hitung nilai terkecil dari bilangan 10^x")
    x += 1

print("Nilai Terkceil Dari Bilangan 10^ x lebih dari n adalah", 10 ** x)
print("-$$$$ END PROGRAM $$$$-")