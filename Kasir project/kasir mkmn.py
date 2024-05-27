import tkinter as tk
from tkinter import messagebox

# Dictionary untuk menyimpan informasi makanan (nama dan harga)
food_menu = {
    "Nasi Goreng": 15000,
    "Soto": 13000,
    "Mie Ayam": 10000,
    "Bakso": 15000,
    "Mie Goreng": 10000,
    "Rawon": 18000,
    "Gado-Gado": 14000,
    "Nasi Kuning": 12000,
    "Ayam Goreng": 17000,
    "Nasi Rendang": 15000,
}

# Dictionary untuk menyimpan informasi minuman (nama dan harga)
drink_menu = {
    "Es Teh Manis": 5000,
    "Es Jeruk": 9000,
    "Air Mineral": 3000,
    "Aneka Jus": 10000,
    "Es Campur": 10000,
    "Es Cincau": 6000,
    "Soda Gembira": 8000,
    "Teh Tarik": 7000,
    "Kopi Susu": 5000,
    "Es Cendol": 7000
}

def hitung_total_pembelian():
    # Menghitung total pembelian makanan dan minuman
    total_makanan = sum(food_menu[item.split('.')[1].strip()] * int(porsi_entry.get()) for item in makanan_option["menu"].keys())
    total_minuman = sum(drink_menu[item.split('.')[1].strip()] * int(gelas_entry.get()) for item in minuman_option["menu"].keys())
    
    # Menghitung total pembelian sebelum PPN
    total_pembelian = total_makanan + total_minuman
    
    # Update label text
    total_pembelian_label.config(text=f"Total Pembelian: Rp {total_pembelian}")

def hitung_tagihan():
    totalmakanan = 0
    totalminuman = 0
    porsi = 0
    makan = ""
    gelas = 0
    minum = ""
    makanan_dibeli = {}  # Dictionary untuk menyimpan makanan yang dibeli (nama: harga)
    minuman_dibeli = {}  # Dictionary untuk menyimpan minuman yang dibeli (nama: harga)
    
    def hitung_makanan():
        nonlocal totalmakanan
        nonlocal porsi
        nonlocal makan
        
        # Dapatkan string item makanan yang dipilih
        selected_item = makanan_var.get()
        
        # Ekstrak nama makanan dari string yang dipilih
        makan = selected_item.split('. ')[1].split(' (')[0].strip()
        harga = food_menu[makan]
        
        porsi = int(porsi_entry.get())
        totalmakanan = porsi * harga
        
        # Tambahkan makanan ke dalam dictionary
        makanan_dibeli[makan] = totalmakanan

    def hitung_minuman():
        nonlocal totalminuman
        nonlocal gelas
        nonlocal minum
        
        # Dapatkan string item minuman yang dipilih
        selected_item = minuman_var.get()
        
        # Ekstrak nama minuman dari string yang dipilih
        minum = selected_item.split('. ')[1].split(' (')[0].strip()
        harga = drink_menu[minum]
        
        gelas = int(gelas_entry.get())
        totalminuman = gelas * harga
        
        # Tambahkan minuman ke dalam dictionary
        minuman_dibeli[minum] = totalminuman

    hitung_makanan()
    hitung_minuman()
    
    # Menghitung total pembelian makanan dan minuman
    total_pembelian = sum(makanan_dibeli.values()) + sum(minuman_dibeli.values())
    
    # Menghitung total pembelian sebelum PPN
    total_pembelian_sebelum_ppn = total_pembelian
    
    # Menghitung PPN 11%
    ppn = total_pembelian * 0.11
    
    # Total pembelian setelah ditambahkan PPN
    total_pembelian += ppn

    # Update the total purchase amount label
    total_pembelian_label_entry.delete(0, tk.END)
    total_pembelian_label_entry.insert(0, f"Rp {total_pembelian}")
    
    
    # Mengambil jumlah uang yang diberikan pelanggan
    uang_diberikan = int(uang_entry.get())
    
    # Menghitung kembalian
    kembalian = uang_diberikan - total_pembelian
    
    # Create a notification message
    if kembalian >= 0:
        notification_msg = f"Selamat Datang, {pembeli_entry.get()}!\n\nTotal Pembelian (belum termasuk PPN 11%): Rp {total_pembelian_sebelum_ppn}\n\nMakanan yang dibeli:\n"
        for item, price in makanan_dibeli.items():
            notification_msg += f"- {item}: Rp {price}\n"
        notification_msg += "\nMinuman yang dibeli:\n"
        for item, price in minuman_dibeli.items():
            notification_msg += f"- {item}: Rp {price}\n"
        notification_msg += f"\nPPN 11%: Rp {ppn}\nTotal Pembelian (termasuk PPN 11%): Rp {total_pembelian}\n\nUang yang diberikan: Rp {uang_diberikan}\nKembalian: Rp {kembalian}\n\nTerima kasih telah berbelanja!"
    else:
        notification_msg = "Maaf, uang yang diberikan tidak mencukupi untuk pembelian ini. Silakan masukkan uang yang cukup."

    # Show the notification
    messagebox.showinfo("Nota Pembayaran", notification_msg)

    hitung_makanan()
    hitung_minuman()
    
    # Menghitung total pembelian makanan dan minuman
    total_pembelian = sum(makanan_dibeli.values()) + sum(minuman_dibeli.values())
    
    # Menghitung total pembelian sebelum PPN
    total_pembelian_sebelum_ppn = total_pembelian
    
    # Menghitung PPN 11%
    ppn = total_pembelian * 0.11
    
    # Total pembelian setelah ditambahkan PPN
    total_pembelian += ppn

    # Update the total purchase amount label
    total_pembelian_label_entry.delete(0, tk.END)
    total_pembelian_label_entry.insert(0, f"Rp {total_pembelian}")
    
    
    # Mengambil jumlah uang yang diberikan pelanggan
    uang_diberikan = int(uang_entry.get())
    
    # Menghitung kembalian
    kembalian = uang_diberikan - total_pembelian
    
    # Create a notification message
    if kembalian >= 0:
        notification_msg = f"Selamat Datang, {pembeli_entry.get()}!\n\nTotal Pembelian (belum termasuk PPN 11%): Rp {total_pembelian_sebelum_ppn}\n\nMakanan yang dibeli:\n"
        for item, price in makanan_dibeli.items():
            notification_msg += f"- {item}: Rp {price}\n"
        notification_msg += "\nMinuman yang dibeli:\n"
        for item, price in minuman_dibeli.items():
            notification_msg += f"- {item}: Rp {price}\n"
        notification_msg += f"\nPPN 11%: Rp {ppn}\nTotal Pembelian (termasuk PPN 11%): Rp {total_pembelian}\n\nUang yang diberikan: Rp {uang_diberikan}\nKembalian: Rp {kembalian}\n\nTerima kasih telah berbelanja!"
    else:
        notification_msg = "Maaf, uang yang diberikan tidak mencukupi untuk pembelian ini. Silakan masukkan uang yang cukup."

    # Show the notification
    messagebox.showinfo("Nota Pembayaran", notification_msg)

def hitung_tagihan():
    # Inisialisasi total pembelian makanan dan minuman
    total_pembelian_makanan = sum(item[2] for item in keranjang_makanan)
    total_pembelian_minuman = sum(item[2] for item in keranjang_minuman)

    # Menghitung total pembelian sebelum PPN
    total_pembelian_sebelum_ppn = total_pembelian_makanan + total_pembelian_minuman

    # Menghitung PPN 11%
    ppn = total_pembelian_sebelum_ppn * 0.11
    
    # Total pembelian setelah ditambahkan PPN
    total_pembelian = total_pembelian_sebelum_ppn + ppn
    
    # Update label total_pembelian_label_entry
    total_pembelian_label_entry.delete(0, tk.END)
    total_pembelian_label_entry.insert(0, f"Rp {total_pembelian}")

    # Mengambil jumlah uang yang diberikan pelanggan
    uang_diberikan = int(uang_entry.get())
    
    # Menghitung kembalian
    kembalian = uang_diberikan - total_pembelian
    
    # Buat pesan notifikasi
    if kembalian >= 0:
        notification_msg = f"Selamat Datang, {pembeli_entry.get()}!\n\nTotal Pembelian (belum termasuk PPN 11%): Rp {total_pembelian_sebelum_ppn}\n\nMakanan yang dibeli:\n"
        for item in keranjang_makanan:
            notification_msg += f"- {item[0]} ({item[1]} porsi): Rp {item[2]}\n"
        notification_msg += "\nMinuman yang dibeli:\n"
        for item in keranjang_minuman:
            notification_msg += f"- {item[0]} ({item[1]} gelas): Rp {item[2]}\n"
        notification_msg += f"\nPPN 11%: Rp {ppn}\nTotal Pembelian (termasuk PPN 11%): Rp {total_pembelian}\n\nUang yang diberikan: Rp {uang_diberikan}\nKembalian: Rp {kembalian}\n\nTerima kasih telah berbelanja!"
    else:
        notification_msg = "Maaf, uang yang diberikan tidak mencukupi untuk pembelian ini. Silakan masukkan uang yang cukup."

    # Tampilkan pesan notifikasi
    messagebox.showinfo("Nota Pembayaran", notification_msg)


app = tk.Tk()
app.title("Restoran Pak Mbuddd")
app.geometry("600x600")

pembeli_label = tk.Label(app, text="Masukkan nama Pembeli:")
pembeli_label.pack()
pembeli_entry = tk.Entry(app)
pembeli_entry.pack()

makanan_label = tk.Label(app, text="Pilih Makanan:")
makanan_label.pack()

makanan_var = tk.StringVar()
makanan_var.set("")
makanan_option = tk.OptionMenu(app, makanan_var, *["{}. {} (Rp {})".format(num, food, price) for num, (food, price) in enumerate(food_menu.items(), start=1)])
makanan_option.pack()

porsi_label = tk.Label(app, text="Berapa Porsi:")
porsi_label.pack()
porsi_entry = tk.Entry(app)
porsi_entry.pack()

minuman_label = tk.Label(app, text="Pilih Minuman:")
minuman_label.pack()

minuman_var = tk.StringVar()
minuman_var.set("")
minuman_option = tk.OptionMenu(app, minuman_var, *["{}. {} (Rp {})".format(num, drink, price) for num, (drink, price) in enumerate(drink_menu.items(), start=1)])
minuman_option.pack()

gelas_label = tk.Label(app, text="Berapa Gelas:")
gelas_label.pack()
gelas_entry = tk.Entry(app)
gelas_entry.pack()

keranjang_makanan = []
keranjang_minuman = []

def tambah_ke_keranjang_makanan():
    selected_item = makanan_var.get()
    makan = selected_item.split('. ')[1].split(' (')[0].strip()
    harga = food_menu[makan]
    porsi = int(porsi_entry.get())
    totalmakanan = porsi * harga
    keranjang_makanan.append((makan, porsi, totalmakanan))
    update_keranjang_label()
    
def tambah_ke_keranjang_minuman():
    selected_item = minuman_var.get()
    minum = selected_item.split('. ')[1].split(' (')[0].strip()
    harga = drink_menu[minum]
    gelas = int(gelas_entry.get())
    totalminuman = gelas * harga
    keranjang_minuman.append((minum, gelas, totalminuman))
    update_keranjang_label()

def update_keranjang_label():
    keranjang_label.config(text="Keranjang Makanan:\n" + "\n".join([f"{item[0]} ({item[1]} porsi) - Rp {item[2]}" for item in keranjang_makanan]) +
                                  "\n\nKeranjang Minuman:\n" + "\n".join([f"{item[0]} ({item[1]} gelas) - Rp {item[2]}" for item in keranjang_minuman]))

# Setelah definisi label total_pembelian_label_entry, tambahkan label baru untuk menampilkan keranjang
keranjang_label = tk.Label(app, text="Keranjang Belanja:")
keranjang_label.pack()

# Frame untuk tombol "Tambahkan Makanan ke Keranjang"
frame_makanan = tk.Frame(app)
frame_makanan.pack(pady=5)  # Menambahkan jarak di atas frame

tambah_makanan_button = tk.Button(frame_makanan, text="Tambahkan Makanan ke Keranjang", command=tambah_ke_keranjang_makanan)
tambah_makanan_button.pack(padx=10)  # Menambahkan jarak horizontal di sekitar tombol

# Frame untuk tombol "Tambahkan Minuman ke Keranjang"
frame_minuman = tk.Frame(app)
frame_minuman.pack(pady=5)  # Menambahkan jarak di antara frame

tambah_minuman_button = tk.Button(frame_minuman, text="Tambahkan Minuman ke Keranjang", command=tambah_ke_keranjang_minuman)
tambah_minuman_button.pack(padx=10)  # Menambahkan jarak horizontal di sekitar tombol


total_pembelian_label = tk.Label(app, text="Total Pembelian:")
total_pembelian_label.pack()
total_pembelian_label_entry = tk.Entry(app)
total_pembelian_label_entry.pack()

uang_label = tk.Label(app, text="Uang Tunai Pembeli:")
uang_label.pack()
uang_entry = tk.Entry(app)
uang_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_tagihan)
hitung_button.pack()



app.mainloop()