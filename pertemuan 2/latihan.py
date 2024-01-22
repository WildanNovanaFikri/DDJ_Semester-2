Olahraga = ("voli", "senam", "badminton", "lompat", "basket", "futsal")
Olahraga_list = list(Olahraga)
print("tuple = ", Olahraga)
print("List = ", Olahraga_list)
Olahraga_list.append("Tenis")
del Olahraga_list[3]
print(Olahraga_list)
Olahraga_list[5] = "Sepak Bola"
print(Olahraga_list)
Olahraga_tuple = tuple(Olahraga_list)
print(Olahraga_tuple)