angka = int(input("masukkan angka: "))
i = 0 
b = 1
sebelum = 0

while i < angka:    
    a=i
    pertama = a + b
    hasil = pertama + sebelum
    sebelum = hasil
    i += 1  
    print("hasil dari penjumlahan deret 1 hingga "+ str(angka) + ' = ' + str(hasil))
    
    