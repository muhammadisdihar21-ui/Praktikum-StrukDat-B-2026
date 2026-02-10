#dictionary data mahasiswa
mahasiswa = {
    "A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

#1.menampilkan nama mahasiswa dengan IPK di atas 3.5
print("Mahasiswa dengan IPK di atas 3.5:")
for data in mahasiswa.values(): #mengambil semua isi (value) dari dictionary, tanpa memperdulikan keynya
    if data["ipk"] > 3.5:
        print(data["nama"])

#menghitung total IPK
total_ipk = 0
for data in mahasiswa.values(): #mengambil semua isi (value) dari dictionary, tanpa memperdulikan keynya
    total_ipk += data["ipk"]

#menghitung rata-rata IPK
rata_ipk = total_ipk / len(mahasiswa) 
#3.menampilkan rata-rata IPK
print("Rata-rata IPK:", rata_ipk)

#4.menambahkan data mahasiswa baru
mahasiswa["A004"] = {
    "nama": "Isdihar",
    "prodi": "Teknik Informatika",
    "ipk": 4.00
}

#menampilkan data mahasiswa setelah ditambah
print("Data mahasiswa setelah ditambah:")
print(mahasiswa)
