print("\npenggunaan Continue pada Looping")
print("----------------\n")
a = 0
b = float(input("Masukan angka anda : "))
while a < b: # a < b adalah syarat
    a += 1 # Increment
    if a == 5: # Seleksi kondisi
        continue # Continue point
    print(a)
    