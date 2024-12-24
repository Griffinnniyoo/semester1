import os
userName = 'Gi'
password = '10'

nama = str(input('masukan nama :'))
pw = str(input('masukan pasword :'))
salah = 0

while ((nama != userName) or (pw != password)) and (salah < 2):
       salah += 1
       print('pasword atau nama salah ULANGI')
       os.system('pause')
       os.system('cls')
       nama = str(input('masukan nama :'))
       pw = str(input('masukan pasword :'))


if (nama == userName) and  (pw == password) :
       os.system('cls')
       print('BERHASIL LOGINN')
       merk = str(input('\nmasukan merk :'))
       harga = int(input('masukan harga :'))
       dp = int(input('masukan dp       :'))
       lama = int(input('masukan lama angsuran :'))
       while lama != 11 and lama != 17 and lama != 23:
              print('harus antara 11/17/23 ULANGI')
              os.system('pause')
              os.system('cls')
              lama = int(input('masukan lama angsuran :'))
       match(lama):
              case 11 :
                     bunga = 26.53 / 100 
              case 17 :
                     bunga = 35.50 / 100
              case 23 :
                     bunga =  37.96 / 100
       angsuran = (bunga * harga + harga - dp) / lama

       os.system('cls')
       print(f'angsuran anda : {angsuran:>3,.2f}')
       print(f'daftar angsuran untuk {lama} bulan dengan merk motor {merk}')
       sisaAngsuran = lama * angsuran
       for i in range (1, lama +1):
              sisaAngsuran = sisaAngsuran - angsuran
              print(f'angsuran ke {i} Rp.{sisaAngsuran:3>,.2f}')
else :
       print('anda sudah tiga kali login')
