#memindahkan inci ke cm
panjang = int(input("masukan panang"))
lebar = int(input("masukan lebar"))
tinggi = int(input("masukan tinggi"))
inciToCm = 2.54
hasilVolume = (panjang * lebar * tinggi) * inciToCm
print("hasil pindah volume adalah", hasilVolume)

#tidak menggunakan variable tambahan
x = int(input('masukan nilai'))
y = int(input("masukan nilai"))
print("nilai sebelum di rubah", x , y)
x = x + y
y = x - y
x = x - y
print("nilai setelah di ubah", x , y)

#menggunakan variable bantuan
x = int(input('masukan nilai'))
y = int(input("masukan nilai"))
print("nilai sebelum di rubah", x , y)
temp = x 
x = y
y = temp
print("nilai setelah di ubah", x , y)


