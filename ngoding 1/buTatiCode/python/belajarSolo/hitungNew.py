import os

# Input jumlah semester
semester = int(input("\nMasukkan jumlah semester: "))
while semester > 15:
    print('ULANGI! Sistem belum bisa lebih dari 15 semester.')
    os.system('pause')
    os.system('cls')
    semester = int(input("Masukkan semester Anda: "))

semesterAnda = semester

# Dictionary untuk menyimpan pelajaran dan nilai untuk setiap semester
pelNilaiPerSms = {}

# Input daftar pelajaran dan nilai untuk setiap semester
for i in range(1, semesterAnda + 1):
    print(f"\nSemester {i}:")

    # Input jumlah pelajaran untuk semester ini
    jumlah_pelajaran = int(input(f"Masukkan jumlah pelajaran untuk semester {i}: "))
    while jumlah_pelajaran <= 0:
        print("Jumlah pelajaran harus lebih dari 0. ULANGI")
        os.system('pause')
        os.system('cls')
        jumlah_pelajaran = int(input(f"Masukkan jumlah pelajaran untuk semester {i}: "))

    # Input nama-nama pelajaran untuk semester ini
    daftar_pelajaran = []
    for j in range(1, jumlah_pelajaran + 1):
        nama_pelajaran = input(f"Masukkan nama pelajaran ke-{j} untuk semester {i}: ")
        daftar_pelajaran.append(nama_pelajaran)

    # Simpan daftar pelajaran untuk semester ini
    pelNilaiPerSms[f"Semester {i}"] = {"pelajaran": daftar_pelajaran, "nilai": {}}

    # Input nilai untuk setiap pelajaran
    print(f"\nMasukkan nilai untuk semester {i}:")
    for pelajaran in daftar_pelajaran:
        while True:
            try:
                nilai = float(input(f"Masukkan nilai untuk {pelajaran}: "))
                pelNilaiPerSms[f"Semester {i}"]["nilai"][pelajaran] = nilai
                break
            except ValueError:
                print("Nilai harus berupa angka. Silakan coba lagi.")

# Hitung rata-rata keseluruhan
total_nilai = 0
total_pelajaran = 0

for data in pelNilaiPerSms.values():
    total_nilai += sum(data["nilai"].values())
    total_pelajaran += len(data["nilai"])

nilai_rata_rata_semua = total_nilai / total_pelajaran if total_pelajaran > 0 else 0

# Bersihkan layar
os.system('cls')

# Output hasil rata-rata
print("<<< HASIL NILAI ANDA >>>")
for semester, data in pelNilaiPerSms.items():
    print(f"\n{semester}:")
    for pelajaran, nilai in data["nilai"].items():
        print(f"- {pelajaran} : {nilai}")

print("\n>>> RATA-RATA KESELURUHAN <<<")
print(f"Nilai rata-rata keseluruhan: {round(nilai_rata_rata_semua, 2)}")
