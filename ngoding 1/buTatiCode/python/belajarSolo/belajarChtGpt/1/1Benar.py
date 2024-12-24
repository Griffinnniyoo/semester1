import os

nama = 'Gi'
password = '12'
salah = 0

# Login system
validasiNama = str(input('Masukkan nama: '))
validasiPassword = str(input('Masukkan password: '))

while ((nama != validasiNama) or (password != validasiPassword)) and (salah < 2):
    salah += 1
    print('Nama atau password salah, ulangi!')
    os.system('pause')
    os.system('cls')
    validasiNama = str(input('Masukkan nama: '))
    validasiPassword = str(input('Masukkan password: '))

if (nama == validasiNama) and (password == validasiPassword):
    os.system('cls')
    print('\nLOGIN BERHASIL')

    # Input data barang
    namaBarang = str(input('Nama barang: '))
    hargaBarang = int(input('Harga barang: '))
    while hargaBarang <= 0:
        hargaBarang = int(input('Harga barang harus positif, masukkan lagi: '))
    uangMuka = int(input('Uang muka: '))
    while uangMuka < 0 or uangMuka >= hargaBarang:
        uangMuka = int(input('Uang muka harus positif dan kurang dari harga barang: '))
    lamaCicilan = int(input('Lama cicilan [6, 12, 24]: '))

    # Validasi lama cicilan
    while lamaCicilan not in [6, 12, 24]:
        print('HARUS [6/12/24]')
        os.system('pause')
        os.system('cls')
        lamaCicilan = int(input('Lama cicilan [6, 12, 24]: '))

    # Perhitungan bunga
    match lamaCicilan:
        case 6:
            bunga = 10 / 100
        case 12:
            bunga = 20 / 100
        case 24:
            bunga = 30 / 100

    cicilanPerbulan = (hargaBarang * (1 + bunga) - uangMuka) / lamaCicilan
    sisaCicilan = cicilanPerbulan * lamaCicilan

    # Output hasil
    os.system('cls')
    print(f'Cicilan per bulan: Rp. {cicilanPerbulan:,.2f}')
    print('Daftar angsuran:')
    for i in range(1, lamaCicilan + 1):
        sisaCicilan -= cicilanPerbulan
        print(f'Angsuran ke-{i:02}: Rp. {sisaCicilan:,.2f}')
else:
    print('Anda sudah tiga kali salah login!')
