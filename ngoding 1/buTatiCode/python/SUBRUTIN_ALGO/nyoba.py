import os

def menuPilihan():
    
    print('PILIH MENU')
    print('1. A PANGKAT B')
    print('2. barisan 1, 3, 6, 18, 24')
    print('0. keluar')
    pilihMenu = int(input('Masukkan pilihan menu: '))
    while pilihMenu < 0 or pilihMenu > 2:
        print('Pilihan hanya antara 0 sampai 2')
        os.system('pause')
        os.system('cls')
        pilihMenu = int(input('Masukkan pilihan menu: '))
    return pilihMenu

def inputPangkatAB():
    A = int(input('Masukkan nilai A: '))
    B = int(input('Masukkan nilai B: '))
    while B < 0:
        print('Nilai B tidak boleh negatif, ulangi.')
        os.system('pause')
        os.system('cls')
        print(f'Nilai A: {A}')
        B = int(input('Masukkan nilai B: '))
    return A, B

def Pangkat(A, B):
    if B == 0:
        return 1
    else:
        return A * Pangkat(A, B - 1)

def tampilPangkat():
    A, B = inputPangkatAB()
    hasil = Pangkat(A, B)
    print(f'{A} pangkat {B} = {hasil}')

def inputBarisanBanyakSuku():
    N = int(input('Masukkan nilai N: '))
    while N < 1:
        print('Banyak suku tidak boleh kurang dari satu')
        os.system('pause')
        os.system('cls')
        N = int(input('Masukkan nilai N: '))
    return N

def sukuKeN(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        if N % 2 == 1:
            return sukuKeN(N - 2) * sukuKeN(N - 1)
        else:
            return sukuKeN(N - 2) + sukuKeN(N - 1)

def tampilBarisan():
    N = inputBarisanBanyakSuku()
    print('Barisan:')
    for i in range(1, N + 1):
        print(sukuKeN(i), end=' ')
    print()

os.system('cls')
while True:
    pilih = menuPilihan()
    if pilih == 0:
        print('Keluar dari program.')
        break
    elif pilih == 1:
        tampilPangkat()
    elif pilih == 2:
        tampilBarisan()
