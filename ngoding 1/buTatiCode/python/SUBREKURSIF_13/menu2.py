#programMenuPilihan 
# I.S pengguna memilih salah satu nomor menu 
# F.S menampilkan hasil sesuai nomor menu yang di pilih

import os

def MenuPilihan(Pilih):
           os.system('cls')
           print('PILIH MENU')
           print('1. A PANGKAT B')
           print('2. barisan 1, 3, 6, 18, 24')
           print('0. keluar')
           Pilih = int(input('Masukkan pilihan menu: '))
           while (Pilih < 0) or (Pilih > 2):
              print(f'Nomor menu {Pilih} tidak ada ulangi !!')
              os.system('pause')
              os.system('cls')
              print('PILIH MENU')
              print('1. A PANGKAT B')
              print('2. barisan 1, 3, 6, 18, 24')
              print('0. keluar')
              Pilih= int(input('Masukkan pilihan menu: '))
           return Pilih

def IsiA(A):
       A = int(input('\nmasukan harga a : '))
       return A
def IsiB(A,B):
       B = int(input('\nmasukan harga B : '))
       while (B < 0):
              print('gabole negatif ulangi ')
              os.system('pause')
              os.system('cls')
              print('< MENU A PANGKAT B >')
              print(f'nilai A = {A}')
              B = int(input('masukan harga B : '))
       return B

def Pangkat(A,B):
       if (B == 0):
              return 1
       else :
              if (B == 1):
                     return A
              else :
                     return A * Pangkat(A,B-1)

def TampilAPangkatB(A,B):
       A = IsiA(A)
       B = IsiB(A,B)
       print(f'{A} pangkat {B} = {Pangkat(A,B)}')


def BanyakSuku(N):
       N = int(input('banyak suku (N) = '))
       while (N < 1) or  (N > 20):
              print(f'{N} tidak ada, tidak boleh kurang dari 1 dan lebih dari 20 ulangi')
              os.system('pause')
              os.system('cls')
              N = int(input('banyak suku (N) = '))
       return N

def SukuKeN(N):
       if(N == 1):
              return 1
       elif( N == 2 ):
              return 3
       else :
              if(N % 2 == 1):
                     return SukuKeN(N-2) * SukuKeN(N-1)
              else :
                     return SukuKeN(N-2) + SukuKeN(N-1)


def TampilBarisan(N):
       N = BanyakSuku(N)
       print(f'Barisan sebanyak {N} suku adalah ', end ='')
       for i in range(1, N + 1):
              print(SukuKeN(i),end='')
              if (i < N):
                     print(',',end='')
       print('\n')


#badanProgramUtama
Pilih = 0 
Pilih = MenuPilihan(Pilih)

while (Pilih != 0):
       os.system('cls')
       match(Pilih):
              case 1 : 
                     print('< MENU A PANGKAT B >')
                     A = 0
                     B = 0
                     TampilAPangkatB(A,B)
              case 2 :
                     print('< BARISAN 1,3,3,6,18,24 ... >')
                     N = 0
                     TampilBarisan(N)
       os.system('pause')
       os.system('cls')
       Pilih = 0 
       Pilih = MenuPilihan(Pilih)
