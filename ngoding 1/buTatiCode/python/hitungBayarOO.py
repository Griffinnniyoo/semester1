#programMenghitungParkir
# is : memasukan kendaraan nomor polisi jam masuk menit masuk 
# fs : menampilkan biaya parkir dan total bbayar

print("<<<<<<<<<<<PARKIR RACINGGG>>>>>>>>>>")

jenisKendaraan = str(input("nasukan jenis kendaraan :")).upper()
numberPolisi = str(input("nasukan number polisi     :"))
jamMasuk = int(input("jam masuk     [1..12]       :"))
menitMasuk = int(input("menit masuk [0..59]       :"))
jamKeluar = int(input("jam keluar   [1..12]       :"))
menitKeluar = int(input("menit keluar [0..59]       :"))

#badanProgram
if menitKeluar < menitMasuk :
       menitKeluar = menitMasuk + 60
       jamKeluar = jamKeluar - 1
menit = menitKeluar - menitMasuk
if jamKeluar < jamMasuk :
       jamKeluar = jamKeluar + 12
jam = jamKeluar - jamMasuk
if menit > 0 :
       jam = jam +  1
if jenisKendaraan == 'MOTOR':
       biaya = 1500 + (jam - 1) * 500
       keterangan = "motor njir"
else :
       biaya = 3000 + (jam - 1) * 1000
       keterangan = "mobil jir"
#akhirBadanProgram

#menampilkan
print(f'jenis kendaraan     : {jenisKendaraan} ket {keterangan}')
print(f'number polisi       : {numberPolisi}')
print(f'masuk (jam:menit)   : {jamMasuk}:{menitMasuk}')
print(f'keluar (jam:menit)  : {jamKeluar}:{menitKeluar}')
print(f'lama parkir         : {jam} jam :{menit} menit')
print(f'biaya parkir        : Rp.{biaya}')
