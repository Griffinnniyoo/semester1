tanggal = str(input('masukan tanggal [dd/mm/yy] :'))
langganan = str(input('apakah anda langganan ? [Y/T] :')).upper()
# jumlah = int(input('masukan berapa jumblah nya :'))


#CARA SAYA
# if langganan == 'T':
#        hargaPerlembar = 200
#        totalHarga = hargaPerlembar * jumlah
# elif jumlah < 100:
#        hargaPerlembar = 300
#        totalHarga = hargaPerlembar * jumlah
# elif jumlah > 100 :
#        hargaPerlembar = 250
#        totalHarga = hargaPerlembar * jumlah
# else :
#        print('anda bukan langganan')


#CARA IBU

if langganan != 'Y' and langganan != 'T':
       print('langganan harus T DAN Y')
else :
       print('------------------------------------')
       jumlah = int(input('masukan jumlah :'))
       match (langganan) :
              case 'Y' :
                     harga = 200
              case 'T' : 
                     if jumlah < 100:
                            harga = 300
                     else :
                            harga = 250

totalHarga = jumlah * harga


print('------------------------------------')
print(f'anda harus membayar {harga} x {jumlah} = Rp.{totalHarga}')