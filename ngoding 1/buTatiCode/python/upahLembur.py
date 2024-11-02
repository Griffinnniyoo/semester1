# kerja = str(input("apakah and lembur ?"))
# jam = int(input("masukan jam lembur"))

# keterangan = 'anda ga lembur'
# if kerja == "lembur":
#        upah = 10000000
#        jam = upah * jam
#        hasilLembur = upah * 2
#        keteranga  = "anda lembur"

# print(keteranga)
# print (f"anda lembur sekitar {jam}")
# print (f"upah hasil lembur nya yaitu {upah}")
# print(f'hasil lembur yaitu Rp.{hasilLembur}')


# jam = int(input("berapa jam anda bekerja?"))

# upah = 1000000
# keterangan = f'anda ga lembur gaji anda tetap{upah}'
# if jam > 40:
#        lemburPerJam = upah * 2
#        keterangan = f'andalembur total nya yaitu {lemburPerJam}'

# print(keterangan)



# jam = int(input("berapa jam anda bekerja?"))

# gajiPerjam = 100000
# jamKerjaSeminggu = 40 


jam = int(input('masukan jam'))
upahPerjam = 100000

totalUpah = jam * upahPerjam
print(f'anda tida lembur dan gaji anda adalah {jam} jam + upah perjam {upahPerjam}{totalUpah}')

if jam > 40 :
       upahJamLembur = 40 - jam
       upahAwal = 40 * upahPerjam
       upahLembur = upahJamLembur * upahPerjam
       lemburPerjam = upahPerjam * 2
       totalUpah = upahAwal + upahLembur + lemburPerjam
       print(f'jam lembur anda adalah {upahJamLembur} upah awal {upahAwal} upah lembur anda {upahLembur} jadi total upah anda adlaah {totalUpah}')


       


