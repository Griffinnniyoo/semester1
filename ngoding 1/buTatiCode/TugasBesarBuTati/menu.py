#program menu pilihan 

import os 

print('PILIH MENU')
print('-----------')
print('1. kalkulator sederhana')
print('2. Suku ke n dari deret fibonaci')
print('3. S = 2/3 -5/7 + 16/21 -65/81+ ...')
print('0. keluar')

pilih = int(input('pilihan anda? :'))

while (pilih < 0) or (pilih > 3):
       print('nomor menu tidak ada ulangi')
       os.system('pause')
       os.system('cls')
       print('PILIH MENU')
       print('-----------')
       print('1. kalkulator sederhana')
       print('2. Suku ke n dari deret fibonaci')
       print('2. S = 2/3 -5/7 + 16/21 -65/81+ ...')
       print('0. keluar')
       pilih = int(input('pilihan anda? :'))

while pilih != 0 :
       os.system('cls')
       match (pilih):
              case 1 :
                            print('<<<<<<<<<<<<<KALKULATOR SEDERHANA>>>>>>>>>>>>')
                            print('\n')
                            angkaPertama = int(input('masukan angka pertama : '))
                            angkaKedua = int(input('masukan angka kedua : '))
                            operator = str(input('masukan operator : '))
                            while operator != '+' and operator != '-' and operator != ':' and operator != 'x':
                                   hasil = print('harus operator + - : x ULANGG')
                                   os.system('pause')
                                   os.system('cls')
                                   print('\n')
                                   print('<<<<<<<<<<<<<MASUKAN ULANG OPERATOR>>>>>>>>>>>>')
                                   print('\n')
                                   operator = str(input('masukan operator : '))


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
                            

                            print('\n')
                            print('<<<<<<<<<<<<<HASIL KALKULATOR>>>>>>>>>>>>')
                            print(f'angka pertama   = {angkaPertama}')
                            print(f'angka kedua     = {angkaKedua}')
                            print(f'operator        = {operator}')
                            print(f'hasil           = {angkaPertama} {operator} {angkaKedua}')
                            print(f'                = {hasil}')
                                   
              case 2 :
                            print('<<<<<<<<<<<<SUKU KE N DARI DERET FIBONACCI>>>>>>>>>>>>')
                            print('\n')
                           
                            N = int(input("Masukkan nomor suku Fibonacci: "))

                          
                            while (N <= 0):
                                 print("Masukkan nomor suku yang valid (HARUS POSITIFF).")
                                 os.system('pause')
                                 os.system('cls')
                                 print("\n")
                                 print("<<<<<MASUKAN ULANG FIBONACCI>>>>>")
                                 print("\n")
                                 N = int(input("Masukkan nomor suku Fibonacci: "))
                            else:
                                   a = 0
                                   b = 1
                                   if N == 1:
                                          hasil2 = a
                                   elif N == 2:
                                          hasil2 = b
                                   else:
                                          for i in range(2, N + 1):
                                                 c = a + b
                                                 a = b
                                                 b = c
                                                 hasil2 = b      
                            print("(Suku Ke-N dari Fibonacci)")
                            print("\nSuku Ke :", N)
                            print(f"Suku Ke-{N} dari Deret Fibonacci adalah {hasil2}")
              case 3 :

                               
                            print("<<<<<<<<<<<< MENGHITUNG S DARI DERET >>>>>>>>>>\n")

                            
                            N = int(input("Masukkan banyak suku (N): "))

                            while N <= 0:
                                   print("Masukkan jumlah suku yang valid (HARUS POSITIF).")
                                   os.system('pause')
                                   os.system('cls')
                                   print("\n")
                                   print("<<<<< MASUKKAN ULANG JUMLAH SUKU >>>>>\n")
                                   N = int(input("Masukkan banyak suku (N): "))

                          
                            S = 0
                            keterangan = ""

                            
                            for n in range(1, N + 1): #harusnya for i cuman karna rumus nya n saya janti jadi n
                                   SukuPembilang = 5 * n**3 - 26 * n**2 + 46 * n - 23
                                   SukuPenyebut = 6 * n**3 - 31 * n**2 + 55 * n - 27
                                   suku = SukuPembilang / SukuPenyebut

                                   if n % 2 == 0:  
                                    S -= suku
                                    keterangan += (f" - ({SukuPembilang}/{SukuPenyebut})")
                                   else:  
                                          S += suku
                                   if n == 1:
                                          keterangan += (f"({SukuPembilang}/{SukuPenyebut})")
                                   else:
                                          keterangan += (f" + ({SukuPembilang}/{SukuPenyebut})")

                   
                            print("\n<<<< HASIL PERHITUNGAN >>>>")
                            print(f"Banyak Suku (N) = {N}")
                            print(f"S = {keterangan}")
                            print(f"= {S:.3f}")




              

       os.system('pause')
       os.system('cls')
       print('PILIH MENU')
       print('-----------')
       print('1. kalkulator sederhana')
       print('2. Suku ke n dari deret fibonaci')
       print('3. S = 2/3 -5/7 + 16/21 -65/81+ ...')
       print('0. keluar')

       pilih = int(input('pilihan anda? :'))
