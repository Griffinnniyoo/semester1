import os


jumlahData = int(input('masukan data yang anda perlu :'))


for i in range(jumlahData + 1):
       print(f'masukan data siswa ke {i}')
       namaMahasiswa = str(input('masukan nama mahasiswa :'))
       print(f'masukan nilai untuk {namaMahasiswa}')
       matematika = int(input('masukan nilai mtk :'))
       bahasaInggris = int(input('masukan nilai bahasa inggris :'))
       biologi = int(input('masukan nilai biologi :'))
       rataRataNilai = round(matematika + bahasaInggris + biologi /3)

# rataRataNilai = 0

# for i in range (1, 3):
#        namaMahasiswa = str(input('masukan nama mahasiswa :'))
#        matematika = int(input('masukan nilai mtk :'))
#        bahasaInggris = int(input('masukan nilai bahasa inggris :'))
#        biologi = int(input('masukan nilai biologi :'))
#        rataRataNilai = round(matematika + bahasaInggris + biologi /3)

# if rataRataNilai > rataRataNilai:
#        print(f'\nnama mahasiswa :{namaMahasiswa}')
#        print(f'matematika :{matematika}')
#        print(f'bahasaInggris :{bahasaInggris}')
#        print(f'biologi :{biologi}')