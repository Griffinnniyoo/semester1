#ProgramMenghitungFaktorial
#I.S Pengguna memasukan angka yang akan di faktorial kan
#F.S menampilkan hasil perhitungan faktorial dari n
import os

#subRutinMemasukanAngkaYangAkanDiFaktorialKan
def IsiN(N):
       os.system('cls')
       print('MENGHITUNG FAKTORIAL (REKURSIF)')
       N = int(input('\nmasukan nilai N :'))
       while (N < 0):
              print('gabole negatif ulangi')
              os.system('pause')
              os.system('cls')
              print('MENGHITUNG FAKTORIAL (REKURSIF)')
              N = int(input('\nmasukan nilai N :'))
       return N

def hitungFaktorial(N):
       if (N == 0) or (N == 1):
              return 1
       else:
              return N * hitungFaktorial(N - 1)

def tampilFaktorial(N):
       print(f'{N}! = {hitungFaktorial(N)}')
#badanProgramUtama
N = 0
N = IsiN(N)
tampilFaktorial(N)
