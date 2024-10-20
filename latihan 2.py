#input bilangan dari pengguna 
bilangan = float(input("masukkan sebuah bilangan: "))
#struktur percabangan
if bilangan > 0: 
    print("bilangan tersebut adalah positif.")
elif bilangan < 0: 
    print("bilangan tersebut adalah negatif.")
else:
    print("bilangan tersebut adalah nol.")