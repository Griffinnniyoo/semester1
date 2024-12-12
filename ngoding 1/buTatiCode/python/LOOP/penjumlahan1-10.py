#ProgramMenjumlahkan1Sampai10
# I.S di berikan pencacah i = 10
# F.S menampilkan hasil penjumlahan (hasil) = 1 + 2 + 3 + .. + 10

#badanProgram
print('PROGRAM PENJUMLAHAN')
print('-------------------')
print('\nPENGULANGAN FOR POSITIF')
print(f'hasil = ',end = '')
Hasil = 0
for i in range(1,11): # format hitung nya  0 - 1 - 2 - 3 sama seperti 1 - 2 - 3 - 4
       print(i, end = '')
       if i < 10:
              print(' + ', end = '')
       Hasil = Hasil + i # bisa juga memakai (Hasil += i)

#output
print(f'\n      =', Hasil)


print('\nPROGRAM PENJUMLAHAN')
print('-------------------')
print('\nPENGULANGAN FOR NEGATIF')
print(f'hasil = ',end = '')
Hasil = 0
for i in range(10,0,-1): # format hitung nya  0 - 1 - 2 - 3 sama seperti 1 - 2 - 3 - 4
       print(i, end = '')
       if i > 1:
              print(' + ', end = '')
       Hasil = Hasil + i # bisa juga memakai (Hasil += i)

#output
print(f'\n      =', Hasil)


print('\nPROGRAM PENJUMLAHAN')
print('-------------------')
print('\nPENGULANGAN WHILE CACAH NAIK')
print(f'hasil = ',end = '')
Hasil = 0
i = 1
while(i <= 10): # format hitung nya  0 - 1 - 2 - 3 sama seperti 1 - 2 - 3 - 4
       print(i, end = '')
       if i <= 10:
              print(' + ', end = '')
       Hasil = Hasil + i # bisa juga memakai (Hasil += i)
       i += 1

#output
print(f'\n      =', Hasil)



print('\nPROGRAM PENJUMLAHAN')
print('-------------------')
print('\nPENGULANGAN WHILE CACAH TURUN')
print(f'hasil = ',end = '')
Hasil = 0
i = 10
while i >= 1: # format hitung nya  0 - 1 - 2 - 3 sama seperti 1 - 2 - 3 - 4
       print(i, end = '')
       if i > 1:
              print(' + ', end = '')
       Hasil = Hasil + i # bisa juga memakai (Hasil += i)
       i -= 1

#output
print(f'\n      =', Hasil)