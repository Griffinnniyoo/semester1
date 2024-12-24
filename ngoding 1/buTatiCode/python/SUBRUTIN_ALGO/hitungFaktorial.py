#Program MenghitungFaktorial
#I.S pengguna memasukan harga yang akan difaktorialkan 
#F.S menghasilkan harga yang di faktorialkan
import os

def IsiN(N): 
       os.system('cls')
       print('<<<<<<PROGRAM MENGHITUNG FAKTORIAL>>>>>>')
       N = int(input('harga yang akan di faktorialkan (N):'))
       while N < 0 :
              print('harga n tidak bole negatif')
              os.system('pause')
              os.system('cls')
              print('<<<<<<PROGRAM MENGHITUNG FAKTORIAL>>>>>>')
              N = int(input('harga yang akan di faktorialkan (N):'))
       return N

def faktorial(N):
       if (N == 0) or (N == 1):
              return 1
       else :
              faktorialN = 1
              for i in range (N, 1, -1) :
                     faktorialN = faktorialN * i
              return faktorialN
       
def tampilFaktorial(N) :
       print(f'{N:2}! = {faktorial(N)}')
       if N > 1:
              for i in range (N, 0, -1):
                     print(i,end='')
                     if i > 1 :
                            print(' x ', end='')
              print('\n =', end='')
       print(f'{faktorial(N)}')

#Badan Program Utama
N = 0 
N = IsiN(N)
tampilFaktorial(N)
