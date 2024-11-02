dataStr =  input("masukan data anda, ")
print("data anda adalah", dataStr, type(dataStr))

dataInt =  int(input("masukan nilai anda"))
print("data anda adalah", dataInt, type(dataStr))

dataFloat = float(input("masukan nilai float"))
print("data anda adalah", dataFloat, type(dataFloat))

#nilai boolean harus di casting menjadi int jika ingin mrnapilkan hasil false
boolean = bool(int(input('input nilai anda')))
print("data anda adalah", boolean, type(boolean))
