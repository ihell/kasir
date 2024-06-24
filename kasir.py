menu = {
    "Ayam Geprek":15000,
    "Lontong Sayur":10000,
    "French Fries":10000,
    "Lemon Tea":5000,
    "Milkshake":25000
}
print("=================== Daftar Menu ===================")
for i in menu:
    print("Daftar Menu : ", i, "\t Harga : ", menu[i])
print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
print("===================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : ")) 
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

print("=================== Detail Pembayaran ===================")
print("Menu yg dipesan          : ", beli)
print("Jumlah yang dipesan      : ", jumlah)
print("Total Biaya              : ", bayar)
print("Total yang harus dibayar : ", total)