mapel = ("matematika", "DDJ", "Olahraga", "Jepang")

mapel_list = list(mapel)
print("tuple = ", mapel)
print("List = ", mapel_list)
mapel_list.append("English")
mapel_list[0] = "informatika"
del mapel_list[2]
print(mapel_list)
mapel_tuple = tuple(mapel_list)
print(mapel_tuple)