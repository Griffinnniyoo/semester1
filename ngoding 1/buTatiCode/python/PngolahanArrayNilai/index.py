#programPegolahanDataNilaiMahasiswa
#i.s pengguna memasukan array nim, nama mahasiswa dan nilai (1:n)
#f.s menampilkan data nilai mahasiswa (1:n) yang sudah terurut
import os

#konstanta
MAKSMHS = 10

#subrutin menentukan indeks nilai 
def IndeksNilai(Nilai):
       if (80 <= Nilai <= 100):
              return 'A'
       elif (70 <= Nilai < 80):
              return 'B'
       elif (60 <= Nilai < 70):
              return 'C'
       elif (50 <= Nilai < 60):
              return 'D'
       else:
              return 'E'

#subrutin memasukan elemen array nim, nama mahasiswa, dan nilai akhir 
def IsiDataMhs(NIM, Nama, NA, Indeks):  
       i = 0
       print(f'Data nilai mahasiswa ke {i+1}')
       print(f'----------------------------')
       # Memasukan elemen nim pertama
       NIM[i] = str(input('Nomor Induk Mahasiswa   : ')).upper()
       while NIM[i] != 'STOP':
              # Memasukan nama mahasiswa dan nilai akhir
              Nama[i] = str(input('Nama Mahasiswa          : ')).upper()
              NA[i]   = float(input('Nilai Akhir             : '))
              # Validasi nilai akhir tidak boleh kurang dari 0 atau lebih dari 100
              while NA[i] < 0 or NA[i] > 100:
                     print("Nilai akhir harus antara 0 dan 100.")
                     NA[i] = float(input('Nilai Akhir             : '))

              Indeks[i] = IndeksNilai(NA[i])

              # Memasukan elemen nim berikutnya
              i = i + 1
              print()
              print(f'Data nilai mahasiswa ke {i+1}')
              print(f'----------------------------')
              NIM[i] = str(input('Nomor Induk Mahasiswa   : ')).upper()

       N = i
       return N

#subrutin menampilkan data nilai mahasiswa
def TampilDataMHS(NIM, Nama, NA, Indeks, Kelas, MatKul, N):
       print('                   DAFTAR NILAI MAHASISWA')
       print(f'Kelas       : {Kelas}')
       print(f'Mata Kuliah : {MatKul}')
       print('-----------------------------------------------------------')
       print('| No |    Nim    |    Nama Mahasiswa    | Nilai | Indeks | ')
       print('-----------------------------------------------------------')
       for i in range(N):
              print(f'| {i+1:>2} | {NIM[i]:9} | {Nama[i]:20} | {NA[i]: >5.1f} | {Indeks[i]:1}      |')
       print('-----------------------------------------------------------')

#subrutin mengurutkan nim secara ascending (bubble sort)
def susunNimAsc(NIM, Nama, NA, Indeks, N):
              for i in range(N - 1):
                     j = N
              while(j >= i + 1):
                     if (NIM[j] < NIM[j-1]):
                            #tukar nim
                            Temp = NIM[j]
                            NIM[j] = NIM[j-1]
                            NIM[j-1] = Temp

                             #tukar nama
                            Temp = Nama[j]
                            Nama[j] = Nama[j-1]
                            Nama[j-1] = Temp

                             #tukar nilai
                            Temp = NA[j]
                            NA[j] = NA[j-1]
                            NA[j-1] = Temp

                             #tukar indeks
                            Temp = Indeks[j]
                            Indeks[j] = Indeks[j-1]
                            Indeks[j-1] = Temp
                     j -= 1 



#badanProgramUtama
# Penciptaan array nim, nama mahasiswa (nama), nilai akhir (na), dan indeks
NIM = [''] * MAKSMHS
Nama = [''] * MAKSMHS
NA = [0] * MAKSMHS
Indeks = [''] * MAKSMHS

# Memasukan kelas dan mata kuliah 
print('PENGISIAN DATA NILAI MAHASISWA')
Kelas = str(input('Kelas        : '))
MatKul = str(input('Mata Kuliah  : '))

N = IsiDataMhs(NIM, Nama, NA, Indeks)
os.system('cls')

# Memanggil subrutin tampil data nilai
print('<<DATA NILAI SEBELUM TERURUT>>')    
TampilDataMHS(NIM, Nama, NA, Indeks, Kelas, MatKul, N)
os.system('pause')
print()
print('<<DATA TERURUT BERDASARKAN NIM SECARA ASCENDING (BUBBLE SORT)>>')   
susunNimAsc(NIM, Nama, NA, Indeks, N) 
TampilDataMHS(NIM, Nama, NA, Indeks, Kelas, MatKul, N)
