def berangkat_sekolah(pakaian, buku):
    if pakaian == "seragam" and buku == "bawa":
        print("Berangkat sekolah")
    else:
        print("Pergi main")

def nama_siswa(nama):
    print(nama)

print(nama_siswa("Raihan")),berangkat_sekolah("seragam", "bawa")            
print(nama_siswa("murti")),berangkat_sekolah("jeans", "tidak membawa buku")            
print(nama_siswa("Adi")),berangkat_sekolah("seragam", "tidak membawa buku")            

