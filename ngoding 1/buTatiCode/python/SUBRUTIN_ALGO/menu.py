# I.S pengguna memilih salah satu nomor menu 
# F.S menampilkan hasil sesuai nomor menu yang di pilih
import os


def menuPilihan(pilih):
       print('<<<<PILIH MENU>>>>')
       print('1. kalkulator sederhana')
       print('2. Suku ke n dari deret fibonaci')
       print('2. S = 2/3 -5/7 + 16/21 -65/81+ ...')
       print('0. keluar')
       pilih = int(input('pilihan anda? :'))
       while (pilih < 0) or (pilih > 3):
              print('nomor menu tidak ada ')
              os.system('pause')
              os.system('cls')
              print('<<<<PILIH MENU>>>>')
              print('1. kalkulator sederhana')
              print('2. Suku ke n dari deret fibonaci')
              print('2. S = 2/3 -5/7 + 16/21 -65/81+ ...')
              print('0. keluar')
              pilih = int(input('pilihan anda? :'))

       return pilih

def Hitung(angkaPertama, angkaKedua, operator):
              match(operator) :
                     case '+' :
                            hasil = angkaPertama + angkaKedua
                     case '-' :
                            hasil = angkaPertama - (angkaKedua)
                     case ':' :
                            hasil = angkaPertama / angkaKedua
                     case '/' :
                            hasil = angkaPertama / angkaKedua
                     case 'x' :
                            hasil = angkaPertama * angkaKedua
              return hasil

def tampilHasil(angkaPertama, angkaKedua, operator):
              print('\n')
              print('<<<<<<<<<<<<<HASIL KALKULATOR>>>>>>>>>>>>')
              print(f'hasil           = {angkaPertama} {operator} {angkaKedua}')
              print(f'                = {Hitung(angkaPertama,angkaKedua,operator)}')

def IsiN(N):
              N = int(input("Masukkan nomor suku Fibonacci: "))
              while (N <= 0):
                     print("Masukkan nomor suku yang valid (HARUS POSITIFF).")
                     os.system('pause')
                     os.system('cls')
                     print("\n")
                     print("<<<<<MASUKAN ULANG FIBONACCI>>>>>")
                     print("\n")
                     N = int(input("Masukkan nomor suku Fibonacci: "))
              return N
def sukuFibonaci(N):
        if(N == 1) or (N == 2):
                return 1
        else :
                sukuke1 = 1
                sukuke2 = 1
                for i in range (2,N):
                     Fibo = sukuke1 + sukuke2
                     sukuke1 = sukuke2
                     sukuke2 = Fibo
                return Fibo
        
def TampilFibonaci(N):
              print(f"Suku Ke-{N} dari Deret Fibonacci adalah {sukuFibonaci(N)}")
        


def banyakSukuN(N):
              N = int(input("Masukkan nomor suku S: "))
              while (N <= 0):
                     print("Masukkan nomor suku yang valid (HARUS POSITIFF).")
                     os.system('pause')
                     os.system('cls')
                     print("\n")
                     print("<<<<<MASUKAN SUKU S>>>>>")
                     print("\n")
                     N = int(input("Masukkan nomor suku suku S: "))
              return N
        
def HitungS(N):
        penyebut = 1
        pembilang = 1 
        s = 0
        for i in range(1,N+1):
                temp = pembilang
                pembilang = pembilang * i + 1
                penyebut = pembilang + temp
                if i % 2 == 1:
                        s = s + pembilang/penyebut
                else:
                        s = s - pembilang/penyebut
        return s

def TampilS(N):
              print("\n<<<< HASIL PERHITUNGAN >>>>")
              print(f"Banyak Suku (N) = {N}")
              print(f"= {N:.3f}")

#badan program utama
os.system('cls')
pilih = 0
pilih = menuPilihan(pilih)
while pilih != 0:
       os.system('cls')
       match(pilih):
              case 1 :
                     os.system('cls')

                     #memasukan satu operan dan satu operator
                     print('<<<<<<<<<<<<<KALKULATOR SEDERHANA>>>>>>>>>>>>')
                     print('\n')
                     angkaPertama = int(input('masukan angka pertama : '))
                     angkaKedua = int(input('masukan angka kedua : '))
                     operator = str(input('masukan operator : '))
                     while operator != '+' and operator != '-' and operator != ':' and operator != 'x':
                                   print('harus operator + - : x ULANGG')
                                   os.system('pause')
                                   os.system('cls')
                                   print('\n')
                                   print('<<<<<<<<<<<<<MASUKAN ULANG OPERATOR>>>>>>>>>>>>')
                                   print('\n')
                                   print(f'angka pertama = {angkaPertama}')
                                   print(f'angka kedua = {angkaKedua}')
                                   operator = str(input('masukan operator : '))
                     tampilHasil(angkaPertama,angkaKedua,operator)

              case 2 :
                     os.system('cls')
                     print('SUKU KE N DARI DERET FIBONACI')
                     N = 0
                     N = IsiN(N)
                     TampilFibonaci(N)
              case 3 :
                     os.system('cls')
                     print('MENGHITUNG NILAI S')
                     N = 0
                     N = banyakSukuN(N)
                     TampilS(N)
       os.system('pause')
       os.system('cls')
       pilih = menuPilihan(pilih)
              

