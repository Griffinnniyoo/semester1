import os

print('<<  PROGRAM PERKALIAN OPERATOR ++ >>')
M = int(input('Masukan nilai M :'))
while (M < 0) or (M > 20) :
       print('harus antara 1 - 20')
       os.system('pause')
       os.system('cls')
       print('<<  PROGRAM PERKALIAN OPERATOR ++ >>')
       M = int(input('Masukan nilai M :'))


N = int(input('Masukan nilai N :'))
while (N < - 5) or (N > 15):
       print('harusa antara -5 - 15')
       os.system('pause')
       os.system('cls')
       print('<<  PROGRAM PERKALIAN OPERATOR ++ >>')
       #MENAMPILKAN HARGA M
       print(f'nilai M ={M}')
       N = int(input('Masukan nilai N :'))

print('<<<<<<<<<<<<<<HASILNYA>>>>>>>>>>>>>>>')

Kali = M * N

print(f'{M:<2}X {N:<2}= ', end='')
if M == 0 or N == 0:
       Kali = 0
elif M == 1:
       Kali = N
else :
        Kali = 0
for i in range(M):
       print(N, end = '')
       if i < M-1 :
              print(' + ', end='')
       Kali = Kali + N
print('\n      = ',end = '')

print(f'  {Kali}')

    