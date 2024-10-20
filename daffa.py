# input pengeluaran
jumlah_pengeluaran = float(input("Masukkan Jumlah Pengeluaran Bulanan: "))

# menentukan kategori
if jumlah_pengeluaran >= 8000000 :
    kategori = "Pengeluaran Tinggi"
elif jumlah_pengeluaran >= 2200000:
    kategori = "Pengeluaran Sedang"
elif jumlah_pengeluaran >= 500000:
    kategori = "Pengeluaran Rendah"
else:
    kategori = "Pengeluaran Sangat Rendah"

# Menampilkan Hasil Kategori
print(f"Kategori Nilai Anda: {kategori}")

