Bulan = str(input("masukan bulan :"))
Tahun = str(input("masukan tahun :"))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

Nik1 = str(input("masukan nik anda"))
Nama = str(input("masukan nama anda"))
GajiPokok1 = int(input("masukan gaji anda Rp."))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

Ppn1 = int(0.1 * GajiPokok1 ) 
Tunjangan1 = int(0.2 * GajiPokok1)
GajiBersih1 = int(GajiPokok1 + Tunjangan1 - Ppn1)

print("pajak ppn anda adalah Rp.", Ppn1)
print("Tunjangan anda adalah Rp.", (Tunjangan1)) 
print("Gaji pokok ppn anda adalah Rp.", (GajiPokok1))
print("Gaji bersih anda adalah Rp. ", (GajiBersih1))
