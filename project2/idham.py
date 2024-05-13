import tkinter as tk
from tkinter import messagebox

def hitung_tagihan():
    totalmakanan = 0
    totalminuman = 0
    porsi = 0
    makan = ""
    gelas = 0
    minum = ""
    makanan_dibeli = []  # List untuk menyimpan makanan yang dibeli
    minuman_dibeli = []  # List untuk menyimpan minuman yang dibeli
    
    def hitung_makanan():
        nonlocal totalmakanan
        nonlocal porsi
        nonlocal makan
        
        # Get the selected food item string
        selected_item = makanan_var.get()
        
        # Split the string to extract the number
        nomor = int(selected_item.split('.')[0])
        porsi = int(porsi_entry.get())
        
        if nomor == 1:
            totalmakanan = porsi * 15000
            makan = "Nasi Goreng"
        elif nomor == 2:
            totalmakanan = porsi * 13000
            makan = "Soto"
        elif nomor == 3:
            totalmakanan = porsi * 10000
            makan = "Mie Ayam"
        elif nomor == 4:
            totalmakanan = porsi * 15000
            makan = "Bakso"
        elif nomor == 5:
            totalmakanan = porsi * 12000
            makan = "Mie Goreng"
        
        # Tambahkan makanan ke dalam list
        makanan_dibeli.append(f"{porsi} {makan}")

    def hitung_minuman():
        nonlocal totalminuman
        nonlocal gelas
        nonlocal minum
        
        # Get the selected drink item string
        selected_item = minuman_var.get()
        
        # Split the string to extract the number
        nomor = int(selected_item.split('.')[0])
        gelas = int(gelas_entry.get())
        
        if nomor == 1:
            totalminuman = gelas * 5000
            minum = "Es Teh Manis"
        elif nomor == 2:
            totalminuman = gelas * 7000
            minum = "Es Jeruk"
        elif nomor == 3:
            totalminuman = gelas * 3000
            minum = "Air Mineral"
        elif nomor == 4:
            totalminuman = gelas * 10000
            minum = "Aneka Jus"
        elif nomor == 5:
            totalminuman = gelas * 10000
            minum = "Es Campur"
        
        # Tambahkan minuman ke dalam list
        minuman_dibeli.append(f"{gelas} {minum}")

    hitung_makanan()
    hitung_minuman()
    
    totalsemua = totalmakanan + totalminuman
    
    # Mengambil jumlah uang yang diberikan pelanggan
    uang_diberikan = int(uang_entry.get())
    
    # Menghitung kembalian
    kembalian = uang_diberikan - totalsemua
    
    # Create a notification message
    notification_msg = f"Total Belanjaan: Rp {totalsemua}\n\nMakanan yang dibeli:\n"
    for item in makanan_dibeli:
        notification_msg += f"- {item}\n"
    notification_msg += "\nMinuman yang dibeli:\n"
    for item in minuman_dibeli:
        notification_msg += f"- {item}\n"
    notification_msg += f"\nUang yang diberikan: Rp {uang_diberikan}\nKembalian: Rp {kembalian}\n\nTerima kasih telah berbelanja!"
    
    # Show the notification
    messagebox.showinfo("Nota Pembayaran", notification_msg)

app = tk.Tk()
app.title("Program Kasir Restoran")
app.geometry("400x400")

pembeli_label = tk.Label(app, text="Masukkan nama Pembeli:")
pembeli_label.pack()
pembeli_entry = tk.Entry(app)
pembeli_entry.pack()

makanan_label = tk.Label(app, text="Pilih Makanan:")
makanan_label.pack()

makanan_var = tk.StringVar()
makanan_var.set("1")
makanan_option = tk.OptionMenu(app, makanan_var, "1. Nasi Goreng", "2. Soto", "3. Mie Ayam", "4. Bakso", "5. Mie Goreng")
makanan_option.pack()

porsi_label = tk.Label(app, text="Berapa Porsi:")
porsi_label.pack()
porsi_entry = tk.Entry(app)
porsi_entry.pack()

minuman_label = tk.Label(app, text="Pilih Minuman:")
minuman_label.pack()

minuman_var = tk.StringVar()
minuman_var.set("1")
minuman_option = tk.OptionMenu(app, minuman_var, "1. Es Teh Manis", "2. Es Jeruk", "3. Air Mineral", "4. Aneka Jus", "5. Es Campur")
minuman_option.pack()

gelas_label = tk.Label(app, text="Berapa Gelas:")
gelas_label.pack()
gelas_entry = tk.Entry(app)
gelas_entry.pack()

uang_label = tk.Label(app, text="Uang Tunai Pembeli:")
uang_label.pack()
uang_entry = tk.Entry(app)
uang_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_tagihan)
hitung_button.pack()

app.mainloop()
