import os


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
       operator = str(input('masukan operator : '))

match(operator) :
       case '+' :
              hasil = angkaPertama + angkaKedua
       case '-' :
              hasil = angkaPertama - (angkaKedua)
       case ':' :
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

# if operator == '+' :
#        hasil = angkaPertama + angkaKedua
# elif operator == '-' :
#        hasil = angkaPertama - angkaKedua
# elif operator == ':' :
#        hasil = angkaPertama / angkaKedua
# elif operator == 'x' :
#        hasil = angkaPertama * angkaKedua
# else :
#        print('tidak ada operator matematika ULANGG')                 