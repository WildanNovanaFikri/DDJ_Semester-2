data_penjualan = [
    {"buah":"baju", "jumlah":20},
    {"buah":"celana", "jumlah":15},
    {"buah":"Sepatu", "jumlah":25},
    {"buah":"tas", "jumlah":10},
    ]

total_penjualan = 0 
for item in data_penjualan:
    total_penjualan += item["jumlah"]

print("Total_penjualan : ", total_penjualan)