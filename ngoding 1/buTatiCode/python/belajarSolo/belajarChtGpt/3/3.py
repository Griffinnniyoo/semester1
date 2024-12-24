import os
users = {
       'admin' : {'password' : '123', 'role' : 'admin'},
       'user1' : {'password' : '1234', 'role' : 'user'},
}

percobaan = 0
maxPercobaan = 3



while percobaan < maxPercobaan:
       username = str(input('masukan username yang valid :'))
       password = str(input('masukan password yang valid :'))
       if username in users and users[username]['password'] == password:
              role = users[username]['role']
              match(role):
                     case 'admin' :
                            os.system('cls')
                            print('\nLOGIN BERHASIL !!!')
                            print('SELAMAT DATANG DI TAMPILAN ADMIN')
                            print('pilihan :')
                            print('1. tambah transaksi cicilan')
                            print('2. lihat riwayat transaksi')
                            print('0. keluar')
                            pilih = int(input('menu pilihan anda :'))
                            while (pilih < 0) or (pilih > 2):
                                   print('nomber tidak valid ulangi !!!')
                                   os.system('cls')                            
                                   print('SELAMAT DATANG DI TAMPILAN ADMIN')
                                   print('pilihan :')
                                   print('1. tambah transaksi cicilan')
                                   print('2. lihat riwayat transaksi')
                                   print('0. keluar')
                                   pilih = int(input('menu pilihan anda :'))
                      
                     case 'user1':
                            os.system('cls')
                            print('SELAMAT DATANG DI TAMPILAN USER')
              break
       else:
              percobaan += 1 
              os.system('cls')
              print(f'username atau password salah ! percobaan = {percobaan}')
if percobaan == maxPercobaan:
       print(f'akses di tolak anda dudah mencoba lebih dari {percobaan}')
       