#programArraySatuDimensiDanDuaDimensi

# I.S USER MEMILIH SALAH SATU NOMOR MENU
# F.S MENAMPILKAN HASIL SESUAI NOMOR YANG DI PILIH

import os

#konstanta
MAKSANGKA = 10
MAKSBARIS = 5
MAKSKOLOM = 3

#Subrutin Menu Utama
def MenuUtama(Pilih):
       print('<< DAFTAR MENU >>')
       print('1. ARRAY 1 DIMENSI')
       print('2. ARRAY 2 DIMENSI')
       print('0. Keluar')
       Pilih = int(input('masukan pilihan anda :'))
       return Pilih

#menu array satu dimensi
def MenuArray1D(Pilih1):
       print('<< MENU ARRAY 1 DIMENSI >>')
       print('1. PENGISIAN ELEMEN ARRAY ANGKA')
       print('2. PENAMBAHAN ELEMEN ARRAY ANGKA')
       print('3. PENYISIPAN ELEMEN ARRAY ANGKA')
       print('4. PENGHAPUSAN ELEMEN ARRAY ANGKA')
       print('5. PENYAJIAN ELEMEN ARRAY ANGKA')
       print('0. Kembalii Ke manu utama')
       Pilih1 = int(input('masukan pilihan anda :'))
       return Pilih1

#subrutin memasukan elemen array angka
def IsiAngka(Angka, BanyakData):
       for i in range(BanyakData):
              Angka[i] = int(input('Angka ke - {} ='.format(i+1)))

def TambahAngka (Angka,BanyakData, AngkaBaru):
       if (BanyakData < MAKSANGKA):
              Angka[BanyakData] = AngkaBaru 
              print(f'angla { AngkaBaru} nberhsil di tambahkan di posisi ke {BanyakData + 1}')
       else :
              os.system('cls')
              print('DATA SUDAH PENUH')
#subrutin sisip matriks
def SisipAngka(Angka, BanyakData, PosisiSisip, AngkaBaru):
       if (BanyakData < MAKSANGKA):
              PosisiSisip -= 1
              if (PosisiSisip >= 1) and ( PosisiSisip <= BanyakData):
                     for i in range( BanyakData - 1 , PosisiSisip - 1, -1):
                            Angka[i + 1] = Angka[i]
                     Angka[PosisiSisip] = AngkaBaru
                     BanyakData += 1
              else :
                     print('posisi tidak valid')
       else :
              print('data penuh')
       return BanyakData

# subrutn menampilkan array angka
def TampilAngka(Angka, BanyakData):
       for i in range(BanyakData):
              print(f'Angka [{i+1}] = {Angka[i]}')
       
#menu array dua dimensi
def MenuArray2D(Pilih2):
       print('<< MENU ARRAY 2 DIMENSI >>')
       print('1. PENGISIAN ELEMEN MATRIKS A')
       print('2. PENGUBAHAN ELEMEN MATRIKS A')
       print('3. PEHAPUSAN ELEMEN MATRIKS A')
       print('4. PENYAJIAN ELEMEN MATRIKS A')
       print('0. Kembalii Ke manu utama')
       Pilih2 = int(input('masukan pilihan anda :'))
       return Pilih2

#subrutin penciptann matriks a
def PenciptaanMatriks(A):
       for j in range(MAKSBARIS):
              A[j] = [0] * MAKSKOLOM

#subrutin memasukan elemen matriks a
def IsiMatriks(A):
       for i in range(MAKSBARIS):
              for j in range(MAKSKOLOM):
                     A[i][j] = int(input('A[{},{}] ='.format(i+1,j+1)))
                     
#SUBRUTIN MENGUBAH SATU ELEMEN MATRIKS DI POSISISI BARIS DAN KOLOM TERTEBTU
def UbahElemen(A, ElemenBaru,PosisiBaris, PosisiKolom ):
       if (PosisiBaris-1 >= 0) and (PosisiBaris-1 <= MAKSBARIS-1):
              if (PosisiKolom-1 >= 0) and (PosisiKolom-1 <= MAKSBARIS-1):
                     print(f'elemen {A[PosisiBaris-1][PosisiKolom-1]} berhasil di ubah menjadi {ElemenBaru} di baris ke {PosisiBaris} dan kolom ke {PosisiKolom}')
                     A[PosisiBaris-1][PosisiKolom-1] = ElemenBaru
              else :
                     os.system('cls')
                     print('posisi kolom tidak sesuai')
       else :
              os.system('cls')
              print('posisi baris tidak sesuai')
  
#
# subrutn menampilkan ELEME MATRIKS A
def TampilMatriks(A):
       for i in range(MAKSBARIS):
              for j in range(MAKSKOLOM):
                     print(f'    {A[i][j] :>2}', end='    ')
              print()
       
       



#badanProgramUtama
os.system('cls')
Pilih = 0
Pilih = MenuUtama(Pilih)
while Pilih != 0:
       os.system('cls')
       match(Pilih):
              case 1 :
                     Pilih1 = 0
                     Pilih1 = MenuArray1D(Pilih1)
                     #PENCIPTAAN ARRAY ANGKA
                     Angka = [0] * MAKSANGKA
                     while Pilih1 != 0:
                            os.system('cls')
                            match(Pilih1) :
                                   case 1 :
                                          print('<<PENGISIAN ARRAY ANGKA>>')
                                          BanyakData = int(input('banyak data yang akan di olah :'))
                                          #validai banyak data jangan kurang dari satu lebih dari maks angka
                                          IsiAngka(Angka, BanyakData)
                                   case 2 :
                                          print('<<PENAMBAHAN ARRAY ANGKA>>')
                                          AngkaBaru = int(input('angka yang di tambahkan = '))
                                          TambahAngka (Angka,BanyakData, AngkaBaru)
                                          BanyakData = BanyakData + 1
                                   case 3 :
                                          print('<<PENYISIPAN ARRAY ANGKA>>')
                                          PosisiSisip = int(input('posisi sisip ='))
                                          SisipAngka(Angka, BanyakData, PosisiSisip, AngkaBaru)
                                   case 4 :
                                          print('<<PENGHAPUSAN ARRAY ANGKA>>')
                                   case 5 :
                                          print('<<PENYAJIAN ARRAY ANGKA>>')
                                          TampilAngka(Angka, BanyakData)
                            os.system('pause')
                            os.system('cls')
                            Pilih1 = MenuArray1D(Pilih1)

              case 2 :
                     Pilih2 = 0
                     Pilih2 = MenuArray2D(Pilih2)
                     # PENCIPTAAN MATRIKS A
                     A = [0] * MAKSBARIS
                     PenciptaanMatriks(A)
                     while Pilih2 != 0:
                            os.system('cls')
                            match(Pilih2):
                                   case 1 :
                                          print('<<PENGISIAN ELEMEN MATRIKS A>>')
                                          IsiMatriks(A)
                                   case 2 :
                                          print('<<PENGUBAHAN ELEMEN MATRIKS A>>')
                                          ElemenBaru = int(input('elemen baru ='))
                                          PosisiBaris = int(input('posisi baris yang di ubah ='))
                                          PosisiKolom = int(input('posisi Kolom yang di ubah ='))
                                          UbahElemen(A, ElemenBaru,PosisiBaris, PosisiKolom )
                                   case 3 :
                                          print('<<PENGHAPUSAN ELEMEN MATRIKS A>>')
                                   case 4 :
                                          print('<<PENYAJIAN ELEMEN MATRIKS A>>')
                                          TampilMatriks(A)

                            os.system('pause')
                            os.system('cls')
                            Pilih = MenuArray2D(Pilih2)


       os.system('cls')
       Pilih = MenuUtama(Pilih)
