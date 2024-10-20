# Minta pengguna untuk memasukkan nilai ujian dan persentase kehadiran
nilai_ujian = float(input("Masukkan nilai ujian mahasiswa: "))
persentase_kehadiran = float(input("Masukkan persentase kehadiran mahasiswa: "))
	
# Tentukan batas nilai dan persentase kehadiran untuk kelulusan
batas_nilai = 75
batas_kehadiran = 88

# Cek kelulusan mahasiswa
if nilai_ujian >= batas_nilai:
	    if persentase_kehadiran >= batas_kehadiran:
	        status_lulus = True
	    else:
	        status_lulus = False
else:
	status_lulus = False
	
# Tampilkan hasil kelulusan
if status_lulus:
	    print("Mahasiswa lulus!")
else:
    print("Mahasiswa tidak lulus.")	
