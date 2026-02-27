#soal1.a
nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas[3] = 75
print(nilai_tugas)

#soal1.b
nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)
print(nilai_tugas)

#soal1.c
print(sum(nilai_tugas))

#soal1.d
for x in nilai_tugas:
    if x == 100:
        print("Ada nilai sempurna")
        break
    else:
        print("Tidak ada")
        break

#soal2.a
kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]
for nama, nilai in kumpulan_nilai:
    if nilai >= 75:
        print(f"Selamat {nama}, Anda Lulus!")
    else:
        print(f"Maaf {nama}, Anda harus remidi.")

#soal3.a
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

pagi_siang = sesi_pagi & sesi_siang
print("mahasiswa yang hadir di kedua sesi: ", pagi_siang)

#soal3.b
unik = sesi_pagi | (sesi_siang)
print("semua mahasiswa dari kedua sesi tanpa duplikat: ", unik)

#soal3.c
sesi_hari_ini = sesi_pagi | sesi_siang
print(sesi_hari_ini)

#soal4.a
transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}]

transaksi[0]["jumlah"] = 8

#soal4.b
transaksi.append({"produk": "Penggaris", "harga": 3000, "jumlah": 5})
transaksi.append({"produk": "Kertas A4", "harga": 50000, "jumlah": 1})

#soal4.c
print("Ringkasan Transaksi:")
hasil_ringkasan = []

for item in transaksi:
    total = item["harga"] * item["jumlah"]
    hasil_ringkasan.append(f"Produk: {item['produk']} | Total: {total}")

print(" ".join(hasil_ringkasan))
