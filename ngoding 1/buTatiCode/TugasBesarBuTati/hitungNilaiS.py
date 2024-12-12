import os

print("<<<<<<<<<<<< MENGHITUNG S DARI DERET >>>>>>>>>>\n")


N = int(input("Masukkan banyak suku (N): "))


while N <= 0:
    print("Masukkan jumlah suku yang valid (HARUS POSITIF).")
    os.system('pause')
    os.system('cls')
    print("\n")
    print("<<<<< MASUKKAN ULANG JUMLAH SUKU >>>>>\n")
    N = int(input("Masukkan banyak suku (N): "))


S = 0  
detail = ""  


for n in range(1, N + 1):
    SukuPembilang = 5 * n**3 - 26 * n**2 + 46 * n - 23
    SukuPenyebut = 6 * n**3 - 31 * n**2 + 55 * n - 27
    suku = SukuPembilang / SukuPenyebut  

    if n % 2 == 0:  
        S -= suku
        detail += f" - ({SukuPembilang}/{SukuPenyebut})"
    else:  
        S += suku
        if n == 1:
            detail += f"({SukuPembilang}/{SukuPenyebut})"
        else:
            detail += f" + ({SukuPembilang}/{SukuPenyebut})"

print("\n<<<< HASIL PERHITUNGAN >>>>")
print(f"Banyak Suku (N) = {N}")
print(f"S = {detail}")
print(f"= {S:.3f}")
