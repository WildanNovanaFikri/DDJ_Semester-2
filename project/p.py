print("============== RESTORAN MAS MBUD ==============")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmakanan
   global porsi
   global makan
   print ("\n============== Menu Makanan ==============")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Soto - Rp 13000")
   print("3. Mie Ayam - Rp 10000")
   print("4. Bakso - Rp 15000")
   print("5. Mie Goreng - Rp 12000")
   nomor=int(input("Masukan Pilihan 1/2/3/4/5: "))
   porsi=int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmakanan=porsi*15000
       print (porsi," porsi Nasi Goreng = Rp", totalmakanan)
       makan=("Nasi Goreng")
   elif nomor==2:
       totalmakanan=porsi*13000
       print (porsi," porsi Soto = Rp", totalmakanan)
       makan=("Soto")
   elif nomor==3:
       totalmakanan=porsi*10000
       print (porsi, " porsi Mie Ayam = Rp", totalmakanan)
       makan=("Mie Ayam")
   elif nomor==4:
       totalmakanan=porsi*15000
       print (porsi, " porsi Bakso = Rp", totalmakanan)
       makan=("Mie Ayam")
   elif nomor==5:
       totalmakanan=porsi*12000
       print (porsi, " porsi Mie Goreng = Rp", totalmakanan)
       makan=("Mie Goreng")      
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalminuman
   global gelas
   global minum
   print("\n============== Menu Minuman ==============")
   print("1. Es Teh Manis - Rp 5000")
   print("2. Es jeruk - Rp 7000")
   print("3. Air Mineral - Rp 3000")
   print("4. Aneka Jus - Rp 10000")
   print("5. Es Campur - Rp 10000")
   nomor=int(input("Masukan Pilihan 1/2/3/4/5: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalminuman=gelas*5000
       print (gelas," Gelas Es Teh Manis = Rp", totalminuman)
       minum=(" Es Teh Manis")
   elif nomor==2:
       totalminuman=gelas*7000
       print (gelas, " Gelas Es Jeruk = Rp", totalminuman)
       minum=("Es Jeruk")
   elif nomor==3:
       totalminuman=gelas*4000
       print (gelas, " Gelas Air Mineral = Rp", totalminuman)
       minum=("Air Mineral")
   elif nomor==4:
       totalminuman=gelas*10000
       print (gelas, " Gelas Aneka Jus = Rp", totalminuman)
       minum=("Aneka Jus")
   elif nomor==5:
       totalminuman=gelas*10000
       print (gelas, " Gelas Es Campur = Rp", totalminuman)
       minum=("Es Campur")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmakanan+totalminuman

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,makan,"( Rp", totalmakanan,")")
print ("\t\t ",gelas,minum,"( Rp", totalminuman,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)

print("==================================")
print("==================================")