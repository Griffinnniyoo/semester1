#membuat indeks nilai siswa / siswi
#{i.s : user input nilai }
#{f.s : menampilkan hasil output}

#inputan
# nilai = int(input('masukan nilai anda :')) integer
# if nilai >= 80 and nilai <= 100:
#        keterangan = 'nilai anda A'
# elif nilai >= 70 and nilai <= 79:
#        keterangan = 'nilai anda B'

# elif nilai >= 60 and nilai <= 69:
#        keterangan = 'nilai anda D'

# elif nilai >= 50 and nilai <= 59:
#        keterangan = 'nilai anda E'

# else:
#        keterangan = 'nilai ada E'

# print(keterangan)

#bilangan bulat
# nilai = float(input('masukan nilai anda :')) 
# if nilai >= 80 and nilai <= 100:
#        keterangan = 'nilai anda A'
# elif nilai >= 70 and nilai < 80:
#        keterangan = 'nilai anda B'

# elif nilai >= 60 and nilai < 70:
#        keterangan = 'nilai anda D'

# elif nilai >= 50 and nilai < 60:
#        keterangan = 'nilai anda E'

# else:
#        keterangan = 'nilai ada E'

# print(keterangan)


#menyederhanakan kondisi majemuk menjadi
nilai = float(input('masukan nilai anda :')) 
if 80 <= nilai <= 100:
       keterangan = 'nilai anda A'
elif 70 <= nilai < 80:
       keterangan = 'nilai anda B'

elif 60 <= nilai < 70:
       keterangan = 'nilai anda D'

elif 50 <= nilai < 60:
       keterangan = 'nilai anda E'

elif 0 <= nilai < 50:
       keterangan = 'nilai anda E'
#validasi
else:
       keterangan = 'nilai harus antara 0-100'

print(keterangan)


