from kurs import kurs
from konverter import ke_mata_uang, ke_idr
from tabulate import tabulate

def format_rupiah(x):
    s = f"{x:,.2f}"       
    s = s.replace(",", "_") 
    s = s.replace(".", ",") 
    s = s.replace("_", ".") 
    return s

#tampilkan tabel kursnya
print("=== KONVERTER MATA UANG ===")

tabel = []
for k, v in kurs.items():
    tabel.append([k, v])
print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))
print()

#input dari user
dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

#proses konversi
if dari == "IDR":
    hasil = ke_mata_uang(jumlah, ke)
elif ke == "IDR":
    hasil = ke_idr(jumlah, dari)
else: #jika konversi bukan dari dan bukan ke IDR
    idr = ke_idr(jumlah, dari)
    hasil = ke_mata_uang(idr, ke)

#outputnya
print(f"\nHasil: {format_rupiah(jumlah)} {dari} = {format_rupiah(hasil)} {ke}\n")


