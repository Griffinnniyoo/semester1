# def isiPenciptaan(maksAngka):
#     Angka = [0] * maksAngka
#     return Angka

# def tampilPenciptaan(Angka):
#     for i in range(1, len(Angka)):
#         print(f'Data[{i}] = {Angka[i]}')

# def isiTraversal():
#     BanyakData = int(input('Masukkan banyak data: '))
#     return BanyakData

# def tampilTraversal(Angka, BanyakData):
#     for i in range(1, BanyakData + 1):
#         print(f'Data[{i}] = {Angka[i]}')

# def isiPenambahan():
#     AngkaBaru = int(input('Masukkan angka baru: '))
#     return AngkaBaru

# def penambahanAngka(Angka, BanyakData, AngkaBaru, maksAngka):
#     if BanyakData < maksAngka:
#         BanyakData += 1
#         Angka[BanyakData] = AngkaBaru
#         print(f'Data[{BanyakData}] ditambahkan dengan nilai {AngkaBaru}')
#     else:
#         print('Data sudah penuh.')
#     return BanyakData

# def isiPenyisipan():
#     tampilTraversal(Angka, BanyakData)
#     posisiSisip = int(input('anda ingin menyisipkan data keberapa ?'))
#     return posisiSisip

# def penyisipan(Angka, BanyakData, posisiSisip, AngkaBaru ):
#     if (BanyakData < maksAngka):
#         if (posisiSisip >= 1 ) and (posisiSisip <= BanyakData):
#             for i in range 

# maksAngka = 10
# Angka = isiPenciptaan(maksAngka + 1)

# print("Array Awal:")
# tampilPenciptaan(Angka)

# BanyakData = isiTraversal()

# print("\nTraversal Array:")
# tampilTraversal(Angka, BanyakData)

# print("\nPenambahan")
# AngkaBaru = isiPenambahan()
# BanyakData = penambahanAngka(Angka, BanyakData, AngkaBaru, maksAngka)
# tampilTraversal(Angka, BanyakData)
