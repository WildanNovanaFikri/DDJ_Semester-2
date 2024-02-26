Total_Nilai = [
   {"Nilai":"Siswa1", "jumlah":85},
   {"Nilai":"Siswa2", "jumlah":90},
   {"Nilai":"Siswa3", "jumlah":78},
   {"Nilai":"Siswa4", "jumlah":92},
   {"Nilai":"Siswa5", "jumlah":88},
   ]

total_nilai = 0 
for item in Total_Nilai:
    total_nilai += item["jumlah"]

print("total_nilai : ", total_nilai)