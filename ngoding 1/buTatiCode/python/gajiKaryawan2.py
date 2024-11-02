#ProgramPenggajianKaryawan
# I.S : pengguna memasukan bulan dan tahun penggajian, beserta tiga data karyawan yang tterdiri dari NIK, nama karyawan (Nama) dan Gaji pook
#F.S : menampilkan data gaji perkaryawan dan total gaji yang harus di bayar oleh perusahaan 
import os

#badan program
#memasukan bulan dan tahun penggajian

Bulan = str(input("masukan (nama bulan) : "))
Tahun = str(input("masukan tahun (YYYY) : "))

#memasukan gaji karyawan 
print('+++++++++++++++++++++++++++++++++++++')
print('<Masukan Gaji Poko dan Data Anda Yaaa 1>')

Nik1 = str(input("masukan nik anda       : "))
Nama1 = str(input("masukan nama anda     : "))
GajiPokok1 = int(input("masuka GajiPokok anda : Rp. "))

#menghitung pajak, tunjangan dan gaji bersih
Ppn1 = 0.1 * GajiPokok1
Tunjangan1 = 0.2 * GajiPokok1
GajiBersih1 = GajiPokok1 + Tunjangan1 - Ppn1

#menampilkan gaji bersih
os.system('cls')
print('+++++++++++++++++++++++++++++++++++++')
print('<Data dan isi gaji andaa yaaaaaaaaaaa>')

print(f'Bulan               : {Bulan}')
print(f'Tahun               : {Tahun}')
print(f'NIK                 : {Nik1}')
print(f'Nama karyawan       : {Nama1}')
print(f'Gaji Pokok          :Rp.{GajiPokok1:>14,.2f}')
print(f'PPN/pajak 10%       :Rp.{Ppn1:>14,.2f}')
print(f'Tunjangan 20%       :Rp.{Tunjangan1:>14,.2f}')
print(f'Gaji Bersih         :Rp.{GajiBersih1:>14,.2f}')
os.system('pause')

#ProgramPenggajianKaryawan
# I.S : pengguna memasukan bulan dan tahun penggajian, beserta tiga data karyawan yang tterdiri dari NIK, nama karyawan (Nama) dan Gaji pook
#F.S : menampilkan data gaji perkaryawan dan total gaji yang harus di bayar oleh perusahaan 
import os

#badan program
#memasukan bulan dan tahun penggajian

Bulan = str(input("masukan (nama bulan) : "))
Tahun = str(input("masukan tahun (YYYY) : "))

#memasukan gaji karyawan 
print('+++++++++++++++++++++++++++++++++++++')
print('<Masukan Gaji Poko dan Data Anda Yaaa 2>')

Nik2 = str(input("masukan nik anda       : "))
Nama2 = str(input("masukan nama anda     : "))
GajiPokok2 = int(input("masuka GajiPokok anda : Rp. "))

#menghitung pajak, tunjangan dan gaji bersih
Ppn2 = 0.1 * GajiPokok2
Tunjangan2 = 0.2 * GajiPokok2
GajiBersih2 = GajiPokok2 + Tunjangan2 - Ppn2

#menampilkan gaji bersih
os.system('cls')
print('+++++++++++++++++++++++++++++++++++++')
print('<Data dan isi gaji andaa yaaaaaaaaaaa>')

print(f'Bulan               : {Bulan}')
print(f'Tahun               : {Tahun}')
print(f'NIK                 : {Nik2}')
print(f'Nama karyawan       : {Nama2}')
print(f'Gaji Pokok          :Rp.{GajiPokok2:>14,.2f}')
print(f'PPN/pajak 10%       :Rp.{Ppn2:>14,.2f}')
print(f'Tunjangan 20%       :Rp.{Tunjangan2:>14,.2f}')
print(f'Gaji Bersih         :Rp.{GajiBersih2:>14,.2f}')
os.system('pause')

#ProgramPenggajianKaryawan
# I.S : pengguna memasukan bulan dan tahun penggajian, beserta tiga data karyawan yang tterdiri dari NIK, nama karyawan (Nama) dan Gaji pook
#F.S : menampilkan data gaji perkaryawan dan total gaji yang harus di bayar oleh perusahaan 
import os

#badan program
#memasukan bulan dan tahun penggajian

Bulan = str(input("masukan (nama bulan) : "))
Tahun = str(input("masukan tahun (YYYY) : "))

#memasukan gaji karyawan 
print('+++++++++++++++++++++++++++++++++++++')
print('<Masukan Gaji Poko dan Data Anda Yaaa 3>')

Nik3 = str(input("masukan nik anda       : "))
Nama3 = str(input("masukan nama anda     : "))
GajiPokok3 = float(input("masuka GajiPokok anda : Rp. "))

#menghitung pajak, tunjangan dan gaji bersih
Ppn3 = 0.1 * GajiPokok3
Tunjangan3 = 0.2 * GajiPokok3
GajiBersih3 = GajiPokok3 + Tunjangan3 - Ppn3

#menampilkan gaji bersih
os.system('cls')
print('+++++++++++++++++++++++++++++++++++++')
print('<Data dan isi gaji andaa yaaaaaaaaaaa>')

print(f'Bulan               : {Bulan}')
print(f'Tahun               : {Tahun}')
print(f'NIK                 : {Nik3}')
print(f'Nama karyawan       : {Nama3}')
print(f'Gaji Pokok          :Rp.{GajiPokok3:>14,.2f}')
print(f'PPN/pajak 10%       :Rp.{Ppn3:>14,.2f}')
print(f'Tunjangan 20%       :Rp.{Tunjangan3:>14,.2f}')
print(f'Gaji Bersih         :Rp.{GajiBersih3:>14,.2f}')
os.system('pause')
os.system('cls')


print('                                     LAPORAN PENGGAJIAN')
print('                                      ------------------')
print(f'Bulan / Tahun : {Bulan:>8}/{Tahun:4}')
print('---------------------------------------------------------------------------------------------')
print('|     Nik     |     Nama Karyawan     |    Gaji Pokok    |      Pajak      |    Tunjangan   |   Gaji Bersih  |')
print('---------------------------------------------------------------------------------------------')
print(f'|   {Nik1:8}  |    {Nama1:10}   |  Rp. {GajiPokok1:>10,.0f} |  Rp. {Ppn1:>11,.1f} |  Rp. {Tunjangan1:>10,.1f} | {GajiBersih1:>10,.2f}  |')
print('--------------------------------------------------------------------------------------------')
print(f'|   {Nik2:8}  |    {Nama2:10}   |  Rp. {GajiPokok2:>10,.0f} |  Rp. {Ppn2:>11,.1f} |  Rp. {Tunjangan2:>10,.1f} | {GajiBersih2:>10,.2f}  | ')
print('---------------------------------------------------------------------------------')
print(f'|   {Nik3:8}  |    {Nama3:10}   |  Rp. {GajiPokok3:>10,.0f} |  Rp. {Ppn3:>11,.1f} |  Rp. {Tunjangan3:>10,.1f} | {GajiBersih3:>10,.2f}  | ')
print('---------------------------------------------------------------------------------')


#menghitung total gaji yag harus di bayar oleh perusahaan 
TotalGaji = GajiBersih1 + GajiBersih2 + GajiBersih3
print(f'Total Gaji    :R.p {TotalGaji:>14,.2f}')
