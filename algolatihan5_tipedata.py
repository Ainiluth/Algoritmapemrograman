tuple_1= ("Faqih","Nicko","Ageng","Ihsan","Adin")
tuple_2= ("23","42","12","53","64")
tuple_3= ("Puri","Putri","Syifa","Anggun")

print(tuple_1)
print(tuple_2)
print(tuple_3)

# membuat tuple yang bernilai kososng
empty_tuple = ()
print("tuple kosong: ",empty_tuple)

# tuple bernilai integer
int_tuple = (4,6,8,10,12,24)
print("Tuple bernilai integer: ", int_tuple)

# tuple dengan kombinasi tipe data
mixed_tuple = (4,"python",9,3)
print("Tuple dengan type data yang berbeda: ",mixed_tuple)

# tuple bersarang
nested_tuple = ("python", {4: 5, 6: 2, 8:2}, (5,3,5,6))
print("A Tuple bersarang: ",nested_tuple)

print()
print()
print()

# membuat list

identitas = ["Luthfia", 19, "Indonesia"]
prodi_1 = ["Informatika",10]
prodi_2 = ["Sistem Operasi",11]
dosen_1 = [10,"Mr.Mursalim"]
dosen_2 = [11,"Mr.Striawan"]

print("cetak semua data...")
print("-----------------------------------------------------------")
print("Nama : %s, Usia : %d, Negara : %s"%(identitas[0],identitas[1],identitas[2]))
print("Cetak Program Studi...")
print("-----------------------------------------------------------")
print("Program Studi 1:\nNama Prodi Pertama: %s, ID: %d\nProgram Studi Kedua:\nNama Prodi Kedua : %s, ID: %s"%(prodi_1[0],prodi_1[1],prodi_2[0],prodi_2[1]))
print("-----------------------------------------------------------")
print("Dosen Pengampu...")
print("-----------------------------------------------------------")
print("Dosen Informatika: %s, ID %d"%(dosen_1[1],dosen_2[0]))
print("Dosen Sistem Operasi: %s, id: %d"%(dosen_2[1],dosen_2[0]))
print(type(identitas),type(prodi_1),type(prodi_2),type(dosen_1),type(dosen_2))

print()
print()
print()

list = [1,2,3,4,5]

# foword
print("--------------------------------")
print("Luthfiaaini")
print("--------------------------------")
print(list[1])
print(list[3:])
print(list[:1])
print(list[1:3])

# backward
print("--------------------------------")
print("Luthfiaaini")
print("--------------------------------")

print(list[-1])
print(list[-3:])
print(list[:-1])
print(list[-1:-3])
