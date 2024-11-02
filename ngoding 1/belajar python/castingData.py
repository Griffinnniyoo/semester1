#merubah data ke type lain
#nilai boolean jika di ganti akan false jika nilai int 0
#jika float data akan di bulatkan ke bawah misalnya 9.9 jadi 9

data_int = 10
print("data ini adalah data berbentuk", type(data_int), "dari data", data_int)

data_float = float(data_int)

print("data ini di ubah dari", type(data_int), "ke data berbentuk", type(data_float), "dengan hasil", data_float)