import os
users = {'Gio': '1234', 'User2': 'abcd', 'Admin': 'admin123'}
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if username in users and users[username] == password:
        os.system('cls')
        print('LOGIN BERHASIL!')
        print('\nMASUKAN DATA')
        namaBarang = str(input('masukan nama barang :'))
        hargaBarang = int(input('masukan harga barang :'))
        while hargaBarang <= 0 :
            os.system('cls')
            os.system('pause')
            print('HARGA BARANG HARUS POSITIF ULANGI')
            print(f'nama barang  : {namaBarang}')
            hargaBarang = int(input('masukan harga barang :'))
        harga10Persen = hargaBarang * 0.10
        Dp = int(input('masukan uang muka :'))
        while Dp < harga10Persen:
            print('DP LEBIH KECIL DARI HARGA BARANG ULANGI ')
            os.system('pause')
            os.system('cls')
            print(f'nama barang  : {namaBarang}')
            print(f'harga barang : {hargaBarang:3>,.2f}')
            Dp = int(input('masukan uang muka :'))
        lamaCicilan = int(input('masukan lama cicilan :'))
        while lamaCicilan != 6 and lamaCicilan != 12 and lamaCicilan != 24:
            print('TIDAK ADA DI ANTARA ITU[6/12/24] COBA LAGI')
            os.system('pause')
            os.system('cls')
            print(f'nama barang  : {namaBarang}')
            print(f'harga barang : {hargaBarang:3>,.2f}')
            print(f'uang muka    : {Dp:3>,.2f}')
            lamaCicilan = int(input('masukan lama cicilan :'))
       
        bunga = lamaCicilan * 1.5 
        cicilanPerbulan = (hargaBarang * (1 + bunga) - Dp) / lamaCicilan
        sisaCicilan = cicilanPerbulan * lamaCicilan
        os.system('cls')
        print(f'Nama barang        : {namaBarang}')
        print(f'Harga barang       : {hargaBarang:3>,.2f}')
        print(f'Uang muka          : {Dp:3>,.2f}') 
        print(f'lama cicilan       : {lamaCicilan} bulan') 
        print(f'Bunga              : {bunga}%') 
        print(f'Cicilan perbulan   : {cicilanPerbulan:3>,.2f}') 
        for i in range(1, lamaCicilan + 1):
            sisaCicilan -= cicilanPerbulan
            print(f'angsuran ke {i} Rp.{sisaCicilan:3>,.2f}')

            




       
        

    else:
        os.system('cls')
        print('Username atau password salah.')
        attempts += 1


if attempts == max_attempts:
    print('Akses ditolak. Anda telah mencoba 3 kali.')
