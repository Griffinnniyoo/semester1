import os
nilaiRataRataMtk = 0
nilaiRataRataBIndo = 0
nilaiRataRataBinggris = 0
nilaiRataRataBiologi = 0
nilaiRataRataFisika = 0
nilaiRataRataKimia = 0
semester = int(input('masukan semester anda [5/7] :'))

#aku pebgen saat user nya mengkli 4 ototmatis 4 semester
while semester not in [5, 7]:
       print('ULANGI harus di antara [5,7]')
       os.system('pause')
       os.system('cls')
       semester = int(input('masukan semester anda [5/7] :'))

if semester == 5:
       semesterAnda = 5
else :
       semesterAnda = 7

for i in range (1, semesterAnda + 1):
       print(f'\nMasukkan nilai semester {i}:')
       print(f'Sebanyak {semesterAnda} semester')
       Matematika = int(input('\nMasukkan nilai Matematika: '))
       BahasaIndonesia = int(input('Masukkan nilai Bahasa Indonesia: '))
       BahasaInggris = int(input('Masukkan nilai Bahasa Inggris: '))
       Fisika = int(input('Masukkan nilai Fisika: '))
       Kimia = int(input('Masukkan nilai Kimia: '))
       Biologi = int(input('Masukkan nilai Biologi: '))

       nilaiRataRataMtk += Matematika / semesterAnda
       nilaiRataRataBIndo+= BahasaIndonesia / semesterAnda
       nilaiRataRataBinggris += BahasaInggris / semesterAnda
       nilaiRataRataFisika += Fisika / semesterAnda 
       nilaiRataRataKimia += Kimia / semesterAnda
       nilaiRataRataBiologi += Biologi / semesterAnda


nilaiRataRataSemua = round(nilaiRataRataMtk + nilaiRataRataBIndo + nilaiRataRataBinggris + nilaiRataRataFisika + nilaiRataRataFisika + nilaiRataRataBiologi / semesterAnda)
       



os.system('cls')
print('<<< HASIL RATA-RATA NILAI ANDA >>>')
print(f'\nBerikut adalah nilai rata-rata Anda selama {semesterAnda} semester:')
print(f'1. Matematika         : {round(nilaiRataRataMtk, 2)}')
print(f'2. Bahasa Indonesia   : {round(nilaiRataRataBIndo, 2)}')
print(f'3. Bahasa Inggris     : {round(nilaiRataRataBinggris, 2)}')
print(f'4. Fisika             : {round(nilaiRataRataFisika, 2)}')
print(f'5. Kimia              : {round(nilaiRataRataKimia, 2)}')
print(f'6. Biologi            : {round(nilaiRataRataBiologi, 2)}')
print('\n>>> RATA-RATA KESELURUHAN <<<')
print(f'Nilai rata-rata keseluruhan: {round(nilaiRataRataSemua, 2)}')     











