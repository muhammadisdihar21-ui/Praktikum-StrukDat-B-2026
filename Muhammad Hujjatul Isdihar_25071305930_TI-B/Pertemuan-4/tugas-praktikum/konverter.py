from kurs import kurs

def ke_mata_uang(jumlah, kode):
    return jumlah / kurs[kode]

def ke_idr(jumlah, kode):
    return jumlah * kurs[kode]


