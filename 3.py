file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

try:
    with open(file1, 'r') as f:
        text1 = f.read().lower()
except FileNotFoundError:
    print(f"File '{file1}' tidak ditemukan.")
    exit()

try:
    with open(file2, 'r') as f:
        text2 = f.read().lower()
except FileNotFoundError:
    print(f"File '{file2}' tidak ditemukan.")
    exit()


kata1 = set(text1.split())
kata2 = set(text2.split())

katakata = kata1.intersection(kata2)

print("Semua kata-kata yang muncul pada kedua file:")
for kata in sorted(katakata):
    print(kata)