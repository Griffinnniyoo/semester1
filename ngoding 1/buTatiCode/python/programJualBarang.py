print('_________________________________________________') 
print('-----------PROGRAM PENJUALAN BARANG---------')
print('_________________________________________________')              



inputKodeBarang = str(input('masukan kode barang :'))
jumlahBeliBarang = int(input('berapa jumlah yang anda beli :'))
bayarSaldo = int(input('masukan saldo anda :'))

if inputKodeBarang == 'PK01':
       namaBarang = "pakaian"
       hargaSatuanBarang = 75000
elif inputKodeBarang == 'TS02':
       namaBarang = "tas"
       hargaSatuanBarang = 10000
elif inputKodeBarang == 'SP03':
       namaBarang = "sepatu"
       hargaSatuanBarang = 15000
elif inputKodeBarang == 'AK04':
       namaBarang = "aksesoris"
       hargaSatuanBarang = 20000
else :
       print('barang tidak ada di sistem')

hargaTotal = hargaSatuanBarang * jumlahBeliBarang
diskonBarang = str(input('apakah di beri diskon ? [YA/TIDAK] :'))

diskon = 0
totalBayar = hargaTotal
kembalian = totalBayar - bayarSaldo
if diskonBarang == 'YA':
       diberiDiskon = float(input('masukan besaran diskon (%): '))
       diskon = hargaSatuanBarang * (diberiDiskon / 100)
       totalBayar = hargaTotal - diskon
       kembalian = totalBayar - bayarSaldo
       if bayarSaldo < totalBayar:
              print('saldo anda kurang')
              print('_________________________________________________')              
       else :
              print('_________________________________________________')              
              print(f"Kode Barang    : {inputKodeBarang}")
              print(f"Nama Barang    : {namaBarang}")
              print(f"Jumlah Beli    : {jumlahBeliBarang}")
              print(f"Harga Satuan   : Rp {hargaSatuanBarang:,}")
              print(f"Diskon         : Rp {diskon:,}%")
              print(f"Harga Total    : Rp {hargaTotal:,}")
              print(f"Total Bayar    : Rp {totalBayar:,}")
              print(f"Bayar          : Rp {bayarSaldo:,}")
              print(f"Kembalian      : Rp {kembalian:,}")