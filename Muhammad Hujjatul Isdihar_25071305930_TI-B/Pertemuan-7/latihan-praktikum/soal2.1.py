antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    index_tujuan = posisi - 1
    antrean_array.insert(index_tujuan, nama_pasien)
    print(f"--- Menyisipkan {nama_pasien} di posisi {posisi} ---")

    print("Antrian Awal: ")
    print(antrean_array)
    print()

sisipkan_pasien_darurat_array("Pasien DARURAT X", 2)

print("Antrean Akhir (Array):")
for i, pasien in enumerate(antrean_array, 1):
    print(f"{i}. {pasien}")


    