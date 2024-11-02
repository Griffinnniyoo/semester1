#ProgramMenentukanBilanganGenapAtauGanjil
# is : pengguna memasukan sebuah bilangan
# fs : menampilkan keterangan bilagan genap atau bilangan ganjil

#badan program
#memasukan sebuah bilangan
bilangan = int(input("masukan bilangan :"))
#menentukan bilangan genap atau ganjil

if (bilangan % 2 == 0):
       keterangan = "bilangan genap"
else :
       keterangan = "bilangan ganjil"
print(bilangan, 'adalah',keterangan)
