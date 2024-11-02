print("<<<<<<<<<<WELCOME TO PARK STATION HELLLL>>>>>>>>>>")
kendaraan = str(input("masukan kendaraan anda :"))
nomborPolisi = str(input("masukan nombor polisi :"))
jamMasuk = int(input('masukan jam masuk :'))
menitMasuk = int(input("masukan menit masuk :"))
jamKeluar = int(input("masukan jam keluar :"))
menitKeluar = int(input("masukan menit keluar :"))

if menitKeluar < menitMasuk :
       menitKeluar = menitKeluar + 60
       jamKeluar = jamKeluar - 1

menit = menitKeluar - menitMasuk

if jamKeluar < jamMasuk:
       jamKeluar = jamKeluar + 12
jam = jamKeluar - jamMasuk
if menit > 0:
       jam = jam + 1
if kendaraan == 'motor' :
       biaya = 1500 + (jam - 1) * 500
else :
       biaya = 3500 + (jam - 1) * 500

print("<<<<<<<<<<<<<BAYAR BGST>>>>>>>>>>>>>>")
print('Jenis kendaraan: ', (kendaraan))
print('Nomor polisi: ', (nomborPolisi))
print('Jam masuk: ', (jamMasuk),':', (menitMasuk))
print('Jam keluar: ', (jamKeluar),':',  (menitKeluar))
print('Lama parkir: ', (jam), ' jam ', (menit), ' menit')
print('Biaya parkir: Rp ', (biaya))

# print(kendaraan,nomborPolisi,{jamKeluar:menitKeluar},{jamMasuk:menitMasuk})