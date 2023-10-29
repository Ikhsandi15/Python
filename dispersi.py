# data 
# Kelas Pagi : 24 34 43 20 35 31 35 34 37 28
# Kelas Sore : 30 39 28 42 35 32 39 49 33 23
# Kelas Sabtu-Minggu : 30 30 28 22 34 27 29 31 36

kelasPagi = [24,34,43,20,35,31,35,34,37,28]
kelasSore = [30,39,28,42,35,32,39,49,33,23]
kelasSabtuMinggu = [30,30,28,22,34,27,29,31,36]

# 1. Hitung range BB siswa SMP di kelas Pagi
# Rumus rerata untuk dispersi = Xmaks - Xmin
maks = max(kelasPagi)
minim = min(kelasPagi)
jangkauan = maks - minim
# print(jangkauan)
print(f"jadi jangkauan(range) dari BB kelas pagi adalah {jangkauan}")

# 2. Hitung range BB siswa SMP di kelas Sore
maks = max(kelasSore)
minim = min(kelasSore)
jangkauan = maks - minim
print(f"jadi jangkauan(range) dari BB kelas sore adalah {jangkauan}")

# 3. Hitung range BB siswa SMP di kelas Sabtu-Minggu
maks = max(kelasSabtuMinggu)
minim = min(kelasSabtuMinggu)
jangkauan = maks - minim
print(f"jadi jangkauan(range) dari BB kelas sabtu-minggu adalah {jangkauan}")

# 4. Hitung deviasi rata-rata BB siswa SMP di kelas pagi
# rumus deviasi rata-rata : 1. mencari reratanya dulu dengan zigma data(x) dibagi jumlah data / n, 
jml = 0
for data in range(len(kelasPagi)):
    jml = jml + kelasPagi[data]
    rerata = jml / len(kelasPagi)

print("{:.2f}".format(rerata)) # 2 angka dibelakang koma bila ada

# mengurangi nilai data dengan rerata
# 2. nilai data dikurang dengan rerata untuk mendapat nilai mutlak
nilaiMutlak = 0
for i in kelasPagi:
    hasil = i - rerata
    if(hasil < 0):
        hasil = hasil - hasil - hasil
    # print("{:.2f}".format(hasil))
    nilaiMutlak = nilaiMutlak + hasil

print(nilaiMutlak)

# membagi nilaiMutlak dengan jumlah data
hasilAkhir = nilaiMutlak / len(kelasPagi)
print(f"dx = {nilaiMutlak} / {len(kelasPagi)} = " + "{:.2f}".format(hasilAkhir))
