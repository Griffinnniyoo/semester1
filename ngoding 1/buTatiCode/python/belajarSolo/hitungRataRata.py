# # List untuk menyimpan data harian
# data_harian = []

# # Loop untuk input data selama 2 hari
# for i in range(1, 7):
#     print(f'Day {i}')
#     # Input data untuk setiap statistik
#     data = {
#         'day': i,
#         'point': int(input('Masukan point: ')),
#         'rebound': int(input('Masukan rebound: ')),
#         'assist': int(input('Masukan assist: ')),
#         'steals': int(input('Masukan steals: ')),
#         'blocks': int(input('Masukan blocks: ')),
#         'fieldGoalsMade': int(input('Masukan fieldGoalsMade: ')),
#         'fieldGoalsAttempted': int(input('Masukan fieldGoalsAttempted: ')),
#         'threePointMade': int(input('Masukan threePointMade: ')),
#         'threePointAttempted': int(input('Masukan threePointAttempted: ')),
#         'freeThrowMade': int(input('Masukan freeThrowMade: ')),
#         'freeThrowAttempted': int(input('Masukan freeThrowAttempted: '))
#     }
#     # Menyimpan data ke list
#     data_harian.append(data)

# # Menampilkan data setiap hari
# # for data in data_harian:
# #     print(f"\nDay {data['day']} Statistics:")
# #     for key, value in data.items():
# #         if key != 'day':
# #             print(f"  {key}: {value}")

# # Menjumlahkan total poin dari semua hari
# rataRataPoint =  
# print(f"\nTotal Points from all days: {total_points}")
# Variabel untuk menampung total dari semua statistik
rataRataPoints = 0
rataRataRebound = 0
rataRataAssit = 0
ratRataSteals = 0
rataRataBlocks = 0
fitGoals = 0
threePointFit = 0
freeThrowFit = 0

# Loop untuk input data selama 2 hari
for i in range(1, 8):
    print(f'Day {i}')
    # Input data untuk setiap statistik
    point = int(input('Masukan point: '))
    rebound = int(input('Masukan rebound: '))
    assist = int(input('Masukan assist: '))
    steals = int(input('Masukan steals: '))
    blocks = int(input('Masukan blocks: '))
    fieldGoalsMade = int(input('Masukan fieldGoalsMade: '))
    fieldGoalsAttempted = int(input('Masukan fieldGoalsAttempted: '))
    threePointMade = int(input('Masukan threePointMade: '))
    threePointAttempted = int(input('Masukan threePointAttempted: '))
    freeThrowMade = int(input('Masukan freeThrowMade: '))
    freeThrowAttempted = int(input('Masukan freeThrowAttempted: '))

    # hitungRataRata point
    rataRataPoints += round(point / 7)
    rataRataRebound += round(rebound / 7)
    rataRataAssit += round(assist / 7)
    ratRataSteals += round(steals / 7)
    rataRataBlocks += round(blocks / 7)

    if freeThrowFit < 100 and fitGoals < 100 and threePointFit < 100:
        fitGoals += fieldGoalsMade / fieldGoalsAttempted * 100
        threePointFit += threePointMade / threePointAttempted * 100
        freeThrowFit += freeThrowAttempted / freeThrowMade * 100
    else :
        fitGoals = 100
        threePointFit = 100
        freeThrowFit = 100

        


    

    

# Menampilkan total dari semua hari
print("\nYour statistic in 1 mounth")
print(f'Rata rata point per game   : {rataRataPoints}')
print(f'Rata rata rebound per game : {rataRataRebound}')
print(f'Rata rata assist per game  : {rataRataAssit}')
print(f'Rata rata steals per game  : {ratRataSteals}')
print(f'Rata rata block per game   : {rataRataBlocks}')
print(f'FIT GOALS                  : {fitGoals:.2f} %')
print(f'Three Point Fits           : {threePointFit:.2f} %')
print(f'Free Throw Fits            : {freeThrowFit:.2f} %')

