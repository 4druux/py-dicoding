# - Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
# - Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
# - Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
#   dan simpan dalam variabel bernama "total_harga".

belanja_dico = 750000
diskon = 0.1

if belanja_dico > 500000:
    total_harga = belanja_dico - (belanja_dico * diskon)
else:
    total_harga = belanja_dico

print(f"Total belanja Dico adalah {total_harga}ribu")



