belanja = [
    {"buah":"semangka", "harga":12000},
    {"buah":"nanas", "harga":10000},
    {"buah":"mangga", "harga":15000},
    {"buah":"manggis", "harga":10000},
    ]

total_belanjaan = 0 
for item in belanja:
    total_belanjaan += item["harga"]

print("Total Belanja : ", total_belanjaan)    
