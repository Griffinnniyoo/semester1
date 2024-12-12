# hasil = 0 
# for i in range (1, 10):
#        hasil = hasil + i
#        print(f'{i}')
# print(hasil)

# hasil = 0

# for i in range (1, 10, 1):
#        hasil += i
#        print(f'{i}')
# print(hasil)

# hasil = 0

# for i in range (9, 0, -1):
#        hasil += i
#        print(f'{i}')
# print(hasil)


# hasil = 0
# i = 0

# while i < 10:
#        hasil += i
#        i += 1
      
# print(hasil)


# hasil  





# masukanNama1 = int(input('masukan berapa angka yang di input :'))

names = ["gio", "zio", "abdul"]

# for g in range (1, masukanNama1 + 1):
#        name = str(input(f'masukan nama ke {g} :'))
#        names.append(name)

for i in range (len(names)):
       for o in range (i + 1, len(names)):
              if names [i] > names [o]:
                     names [i], names [o] = names [o], names[i]
print(names)
              
              

a = int(input('masukan nilai a :'))
b = int(input('masukan pangkat nya :'))

hasil = 1
for i in range (b):
       hasil *= a

print(hasil)


while true