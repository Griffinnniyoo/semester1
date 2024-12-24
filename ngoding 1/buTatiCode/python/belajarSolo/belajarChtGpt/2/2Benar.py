import os

# Daftar pengguna
users = {'Gio': '1234', 'User2': 'abcd', 'Admin': 'admin123'}
attempts = 0
max_attempts = 3

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Proses login
while attempts < max_attempts:
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if username in users and users[username] == password:
        clear_screen()
        print('LOGIN BERHASIL!')
        print('\nMASUKKAN DATA')
        
        # Input data barang
        namaBarang = str(input('Masukkan nama barang: '))
        hargaBarang = int(input('Masukkan harga barang: '))
        while hargaBarang <= 0:
            print('HARGA BARANG HARUS POSITIF. ULANGI.')
            hargaBarang = int(input('Masukkan harga barang: '))
        
        # Validasi DP minimal 10% dari harga barang
        harga10Persen = hargaBarang * 0.10
        Dp = int(input('Masukkan uang muka: '))
        while Dp < harga10Persen:
            print(f'DP harus minimal 10% dari harga barang ({harga10Persen:,.2f}). ULANGI.')
            Dp = int(input('Masukkan uang muka: '))
        
        # Validasi lama cicilan
        lamaCicilan = int(input('Masukkan lama cicilan (6, 12, 24 bulan): '))
        while lamaCicilan not in [6, 12, 24]:
            print('Lama cicilan hanya bisa 6, 12, atau 24 bulan. ULANGI.')
            lamaCicilan = int(input('Masukkan lama cicilan (6, 12, 24 bulan): '))
        
        # Menentukan bunga berdasarkan lama cicilan
        match lamaCicilan:
            case 6:
                bunga = 0.10  # 10%
            case 12:
                bunga = 0.15  # 15%
            case 24:
                bunga = 0.20  # 20%
        
        # Hitung cicilan per bulan
        cicilanPerbulan = (hargaBarang * (1 + bunga) - Dp) / lamaCicilan
        sisaCicilan = cicilanPerbulan * lamaCicilan
        
        # Tampilkan hasil
        clear_screen()
        print(f'Nama Barang       : {namaBarang}')
        print(f'Harga Barang      : Rp. {hargaBarang:,.2f}')
        print(f'Uang Muka         : Rp. {Dp:,.2f}')
        print(f'Lama Cicilan      : {lamaCicilan} bulan')
        print(f'Bunga             : {bunga * 100}%')
        print(f'Cicilan per Bulan : Rp. {cicilanPerbulan:,.2f}')
        print('\nDaftar Angsuran:')
        print('-' * 30)
        
        for i in range(1, lamaCicilan + 1):
            sisaCicilan -= cicilanPerbulan
            print(f'Angsuran ke-{i}: Sisa Rp. {sisaCicilan:,.2f}')
        break
    else:
        clear_screen()
        print('Username atau password salah. ULANGI.')
        attempts += 1

# Jika gagal login
if attempts == max_attempts:
    print('Akses ditolak. Anda telah mencoba 3 kali.')
