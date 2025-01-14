# nilai = [12, 45, 23, 78, 23, 56]
# cari = 0

# for i in range(len(nilai)):
#        print(f' | ', nilai[i], end='')


# cari = int(input('\nmasukan nilai yang di cari :'))
# for i in range(len(nilai)):
#        if nilai[i] == cari:
#               print(f'nilai i yang di cari adalah ke {i}')
#               break

# def temukanNilaiUnik(A):
#        hasil = []
#        for elemen in A:
#               frekuensi = A.count(elemen)
#               if frekuensi == 1:
#                      hasil.append(elemen)
#        return hasil

# A = [2,23,43,56,98,12,45]
# hasil = temukanNilaiUnik(A)
# print(F'ELEMEN UNIK {hasil}')


# # Array satu dimensi: daftar nilai mahasiswa
# nilai_mahasiswa = [85, 90, 78, 92, 88]

# # Menghitung rata-rata nilai
# rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
# print(f"Rata-rata nilai mahasiswa: {rata_rata}")

# ////////////////////////////////////

# Array dua dimensi: data transaksi penjualan
# transaksi = [
#     ['ID', 'Produk', 'Jumlah', 'Harga'],
#     [1, 'Laptop', 2, 15000000],
#     [2, 'Smartphone', 5, 8000000],
#     [3, 'Monitor', 3, 3000000]
# ]

# # Menampilkan tabel transaksi
# print("Data Transaksi Penjualan:")

# print(len(transaksi))


# ////////////////////////////////////


# Array satu dimensi: daftar barang di gudang menambahkan nombor
# barang_gudang = ['Mesin A', 'Baterai B', 'Monitor C', 'CPU D', 'Keyboard E']

# # Mencetak semua barang dengan indeksnya
# print("Daftar Barang di Gudang:")
# for index, item in enumerate(barang_gudang):
#     print(f"{index + 1}. {item}")


# ////////////////////////////////////

# # Array satu dimensi: daftar nama mahasiswa
# mahasiswa = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# # Array dua dimensi: tabel nilai ujian mahasiswa
# nilai_ujian = [
#     [85, 90, 78],
#     [88, 76, 92],
#     [75, 85, 84],
#     [90, 88, 89], 
#     [90, 88, 89] 
# ]

# # Menampilkan nilai ujian untuk setiap mahasiswa
# print("Nilai Ujian Mahasiswa:")
# for i, nama in enumerate(mahasiswa):
#     nilai_mat = nilai_ujian[i][0]  # Nilai Matematika
#     nilai_ipa = nilai_ujian[i][1]  # Nilai IPA
#     nilai_bahasa = nilai_ujian[i][2]  # Nilai Bahasa Inggris
#     print(f"{nama}: Matematika: {nilai_mat}, IPA: {nilai_ipa}, Bahasa Inggris: {nilai_bahasa}")
