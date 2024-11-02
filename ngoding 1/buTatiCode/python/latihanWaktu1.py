waktuDetik = int(input("masukan waktu anda"))

Mod36 = 3600
waktuHari = int(waktuDetik / 86400)
waktuJam = int(waktuDetik % 86400 /Mod36) 
waktuMenit = int(waktuDetik % 86400  % Mod36 /60)
waktuDetikHasil = int(waktuDetik % 86400) % Mod36 % 60 


print(f'hasilnya {waktuDetik} = {waktuHari} hari {waktuJam} jam {waktuMenit} menit {waktuDetikHasil} detik ')