#Contoh penggunaan semua method set Python

#Membuat set
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#add() berfungsi menambah elemen
A.add(7)  #menambah angka 7 ke set A

#remove() berfungsi menghapus elemen (error jika tidak ada)
A.remove(1)  #menghapus angka 1

#discard() berfungsi menghapus elemen (aman)
A.discard(10)  # tidak error walau tidak ada

#pop() berfungsi menghapus elemen acak
A.pop()  #menghapus satu elemen secara acak

#union() / | berfungsi menggabungkan dua set
union_set = A.union(B)  #gabungan A dan B

#intersection() / & berfungsi sebagai irisan
intersection_set = A.intersection(B)  #elemen yang sama

#difference() / - berfungsi sebagai selisih
diff_set = A.difference(B)  #elemen A yang tidak ada di B

#symmetric_difference() / ^ berfungsi sebagai pembeda dari dua arah
sym_diff = A.symmetric_difference(B)  #elemen yang tidak sama

#issubset() berfungsi mengecek subset
subset_check = {3, 4}.issubset(B)  #cek subset

#issuperset() berfungsi mengecek superset
superset_check = B.issuperset({5})  #cek superset

#isdisjoint() berfungsi mengecek tidak ada irisan
disjoint_check = A.isdisjoint({100, 200})

#update() berfungsi menggabung dan mengubah set
A.update(B)  #menambahkan semua elemen B ke A

#copy() berfungsi menyalin set
A_copy = A.copy()  #salinan set

#clear() berfungsi mengosongkan set
A_copy.clear()  #menghapus semua elemen

#Menampilkan hasil
print(union_set)
print(intersection_set)
print(diff_set)
print(sym_diff)
print(subset_check)
print(superset_check)
print(disjoint_check)
print(A)
