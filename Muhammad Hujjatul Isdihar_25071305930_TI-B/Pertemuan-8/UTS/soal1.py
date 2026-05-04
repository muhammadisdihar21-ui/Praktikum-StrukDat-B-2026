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

def tampilkan_pasien():
    print("===== DATA PASIEN KLINIK =====")
    print(f"{'No':<2} | {'ID':<4} | {'Nama':<5} | {'Usia':<4} | {'Penyakit':<8} | {'Status Bayar'}")
    print("-" * 60)
    
    for i, p in enumerate(pasien_hari_ini, 1):
        status = "Lunas" if p['bayar'] else "Belum Bayar"
        print(f"{i:<2} | {p['id']:<4} | {p['nama']:<5} | {p['usia']:<4} | {p['penyakit']:<8} | {status}")

def filter_belum_bayar():
    belum_bayar = [p['nama'] for p in pasien_hari_ini if not p['bayar']]
    
    belum_bayar.sort()
    
    print("\n===== PASIEN BELUM BAYAR =====")
    for i, nama in enumerate(belum_bayar, 1):
        print(f"{i}. {nama}")
    
    print(f"Total belum bayar: {len(belum_bayar)} pasien")
    return belum_bayar

tampilkan_pasien()
filter_belum_bayar()