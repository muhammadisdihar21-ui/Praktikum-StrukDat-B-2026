#membuat set mata kuliah kelas A
kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
#membuat set mata kuliah kelas B
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

#1.mencari mata kuliah yang diambil oleh kedua kelas 
sama = kelas_A & kelas_B #berfungsi mengambil mata kuliah yang sama di kelas A dan kelas B saja

#2.mencari mata kuliah yang hanya diambil kelas A
hanya_A = kelas_A - kelas_B #berfungsi mengambil mata kuliah yang hanya ada di kelas A

#3.mencari seluruh mata kuliah unik yang diambil oleh kelas A dan kelas B
unik = kelas_A ^ kelas_B #berfungsi mengambil mata kuliah yang hanya ada di salah satu kelas, 
#tapi tidak sama di kedua kelas

#menampilkan hasil
print("Mata kuliah yang diambil kedua kelas:", sama)
print("Mata kuliah yang hanya diambil kelas A:", hanya_A)
print("Seluruh mata kuliah unik:", unik)