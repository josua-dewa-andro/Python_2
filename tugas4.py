# Soal 1
i = int(input('Masukkan angka: '))
if i % 2 == 0:
    print (i, "Adalah Bilangan Genap")
else:
    print (i, "Adalah Bilangan Ganjil")

# Soal 2
a = int(input('Masukkan angka N: '))

jumlah = 0
b = 1

while b <= a :
    jumlah = jumlah + b
    b = b + 1

print (f'jumlah 1 sampai {a} = {jumlah}')
    
# Soal 3
angka = int(input('Masukkan Angka: '))
print ('Tabel perkalian', angka)
for i in range(1, 11):
    print(angka, "x", i, "=", angka * i)