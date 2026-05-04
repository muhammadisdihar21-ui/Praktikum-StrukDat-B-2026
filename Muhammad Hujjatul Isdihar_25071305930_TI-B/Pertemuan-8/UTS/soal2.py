pasien_hari_ini = [
{"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": 
"Flu",   "bayar": False},
{"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": 
"Tifus", "bayar": True},
{"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": 
"Flu",   "bayar": False},
{"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": 
"Maag",  "bayar": True},
{"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": 
"Tifus", "bayar": False},
{"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": 
"Maag",  "bayar": False},
]

def info_klinik():
    data_klinik = ("Klinik Sehat Bersama", "Jl. Merdeka No. 10, Pekanbaru", "0761-12345")
    
    nama, alamat, telp = data_klinik 
    print("\nInfo Klinik:")
    print(f"Nama   : {nama}")
    print(f"Alamat : {alamat}")
    print(f"Telp   : {telp}")

def rekap_penyakit():
    jenis_penyakit_unik = {p['penyakit'] for p in pasien_hari_ini}
    
    print(f"\nJenis Penyakit Unik: {jenis_penyakit_unik}")
    print(f"Jumlah jenis penyakit: {len(jenis_penyakit_unik)}")
    
    rekap = {}
    for penyakit in jenis_penyakit_unik:
        jumlah = sum(1 for p in pasien_hari_ini if p['penyakit'] == penyakit)
        rekap[penyakit] = jumlah
    
    print("Rekap per penyakit:")
    for peny, jml in rekap.items():
        print(f"{peny:<5} : {jml} pasien")
    
    max_pasien = max(rekap.values())
    penyakit_terbanyak = [peny for peny, jml in rekap.items() if jml == max_pasien]
    
    string_penyakit = ", ".join(penyakit_terbanyak)
    print(f"Penyakit terbanyak: {string_penyakit} ({max_pasien} pasien)")

info_klinik()
rekap_penyakit()