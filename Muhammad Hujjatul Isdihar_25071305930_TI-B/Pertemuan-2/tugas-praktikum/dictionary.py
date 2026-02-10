#Contoh penggunaan semua method dictionary Python

#Membuat dictionary
mahasiswa = {
    "nama": "Isdihar",
    "umur": 19,
    "prodi": "Informatika"
}

#get() berfungsi mengambil value berdasarkan key
nama_mhs = mahasiswa.get("nama")  #mengambil nama

#keys() berfungsi mengambil semua key
list_key = mahasiswa.keys()  #daftar key

#values() berfungsi mengambil semua value
list_value = mahasiswa.values()  #daftar value

#items() berfungsi mengambil pasangan key-value
list_item = mahasiswa.items()  #pasangan key dan value

#update() berfungsi menambah atau mengubah data
mahasiswa.update({"umur": 20})  #update umur

#setdefault() berfungsi ambil value, jika tidak ada maka buat
mahasiswa.setdefault("angkatan", 2023)  #menambah key angkatan

#pop() berfungsi menghapus data berdasarkan key
mahasiswa.pop("prodi")  #menghapus jurusan

#popitem() berfungsi menghapus item terakhir
mahasiswa.popitem()  #menghapus item terakhir

#copy() berfungsi menyalin dictionary
salinan = mahasiswa.copy()  #salinan dictionary

#fromkeys() berfungsi membuat dictionary baru dari key
key_baru = ("a", "b", "c")
dict_baru = dict.fromkeys(key_baru, 0)  #value default 0

#clear() berfungsi mengosongkan dictionary
salinan.clear()  #menghapus semua data

# Menampilkan hasil
print(nama_mhs)
print(list_key)
print(list_value)
print(list_item)
print(mahasiswa)
print(dict_baru)
