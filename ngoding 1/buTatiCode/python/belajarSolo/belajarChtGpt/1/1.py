import os
nama = 'Gi'
password = '12'
salah = 0

validasiNama = str(input('masukan nama : '))
validasiPassword = str(input('masukan password : '))

while((nama != validasiNama) or (password != validasiPassword)):
       print('nama atau password salah ULANGI')
       os.system('pause')
       os.system('cls')
       validasiNama = str(input('masukan nama : '))
       validasiPassword = str(input('masukan password : '))

if (nama == validasiNama) and (password == validasiPassword):
       os.system('cls') 
       print('\nLOGIN BERHASIL')
       namaBarang = str(input('nama barang :'))
       hargaBarang = int(input('harga barang :'))
       uangMuka = int(input('uang muka :'))
       lamaCicilan = int(input('lama cicilan  [6,12,24] :'))
       while lamaCicilan != 6 and lamaCicilan != 12 and lamaCicilan != 24:
              print('HARUS [6/12/24]')
              os.system('pause')
              os.system('cls')
              print(namaBarang)
              print(uangMuka)
              lamaCicilan = int(input('lama cicilan  [6,12,24] :'))
       match(lamaCicilan):
              case 6 :
                     bunga = 10 / 100
              case 12 :
                     bunga = 20 / 100
              case 24 :
                     bunga = 30 / 100
       cicilanPerbulan = (hargaBarang * (1 + bunga) - uangMuka) / lamaCicilan
       sisaCicilan = cicilanPerbulan * lamaCicilan
       os.system('cls')
       print(f' cicilan = {cicilanPerbulan:3>,.2f}')
       print('daftar angsuran')
       for i in range (1, lamaCicilan + 1):
              sisaCicilan -= cicilanPerbulan
              print(f'angsuran ke {i} Rp.{sisaCicilan:3>,.2f}')

