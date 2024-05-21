n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}
for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print(data_aplikasi)
daftar_aplikasi_list = []

for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print("Aplikasi yang muncul di semua kategori:",hasil)

satu_kategori = set()
for i in range(len(daftar_aplikasi_list)):
    satu_kategori.difference_update(*daftar_aplikasi_list[:i]+daftar_aplikasi_list[i+1:])
print("Aplikasi hanya muncul di satu kategori: ", satu_kategori)
satu_kategori.clear()


dua_kategori = set()
for i in range(len(daftar_aplikasi_list)):
    dua_kategori.intersection_update(daftar_aplikasi_list[i])
print("Aplikasi yang muncul tepat di dua kategori: ", dua_kategori)
dua_kategori.clear()