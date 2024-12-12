import os
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