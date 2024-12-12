inputKodeBarang = str(input('masukan kode barang :'))
jumlahBeliBarang = int(input('berapa jumlah yang anda beli :'))
bayarSaldo = int(input('masukan saldo anda :'))
# adaDiskon = str('apakah ada diskon ? [YA/TIDAK] :')

tabelBarang = {
    "PK01": {"nama": "Pakaian", "harga_satuan": 75000},
    "TS02": {"nama": "Tas", "harga_satuan": 65500},
    "SP03": {"nama": "Sepatu", "harga_satuan": 157000},
    "AK04": {"nama": "Aksesoris", "harga_satuan": 45000}
}   

if inputKodeBarang not in tabelBarang:
       print('gaada di dalam tabel')
else:
       namaBarang = tabelBarang[inputKodeBarang]["nama"]
       hargaSatuanBarang = tabelBarang[inputKodeBarang]["harga_satuan"]
       namaBarang = tabelBarang[inputKodeBarang]["nama"]
       hargaSatuanBarang = tabelBarang[inputKodeBarang]["harga_satuan"]
       hargaTotal = hargaSatuanBarang * jumlahBeliBarang
       diskonBarang = str(input('apakah di beri diskon ? [YA/TIDAK] :'))
       diskon = 0
       totalBayar = hargaTotal
       kembalian = totalBayar - bayarSaldo
       if diskonBarang == 'YA':
              diberiDiskon = int(input('masukan besaran diskon (%): '))
              diskon = hargaSatuanBarang * (diberiDiskon / 100)
              totalBayar = hargaTotal - diskon
              kembalian = totalBayar - bayarSaldo
  

              
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
            
       
       

