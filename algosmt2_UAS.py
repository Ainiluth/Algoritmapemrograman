import datetime

# tampilan menu
print("============================================================================")
print("                     =>  RESTO MIE JEBRET  <=")
print("                 Jl. Raya Candi, Gondangsari, Clapar")
print("           Kec. Subah, Kabupaten Batang, Jawa Tengah 51262")
print("                    contact person : 083456719905")
print("----------------------------------------------------------------------------")
print("  Spesial GRAND OPENING dapatkan promo diskon 20% minimal belanja 50rb..!")
print(" Promo terbatas dari tgl 24-31 juli 2023, jadi buruan pesen sekarang juga")
print("============================================================================")
print("            ----------------------------------------")
print("            | Kode |    Nama Menu     |    Harga   |")
print("            ----------------------------------------")
print("            |  1   |  Mie Candu Tasty |  Rp 8.500  |")
print("            |  2   |  Mie Jebew Spicy |  Rp 9.000  |")
print("            |  3   |  Udang Kejuh     |  Rp 10.000 |")
print("            |  4   |  Siomay          |  Rp 8.000  |")
print("            |  5   |  Pangsit Goyeng  |  Rp 9.000  |")
print("            |  6   |  Telul Uyung     |  Rp 7.000  |")
print("            |  7   |  Mineral         |  Rp 3.000  |")
print("            |  8   |  Lemon Tea       |  Rp 4.000  |")
print("            |  9   |  Es Coklat       |  Rp 5.000  |")
print("            |  10  |  Es Jeruk        |  Rp 5.000  |")
print("            |  11  |  Teh Tarek       |  Rp 6.000  |")
print("            |  12  |  Mie Setan       |  Rp 25.000 |")
print("            ----------------------------------------")
print("=============================================================================")

# setting waktu
waktu = datetime.datetime.now()
f_waktu = waktu.strftime("%A %x")

n_petugas = input("Masukkan Nama Petugas : ")
mejo = input("Meja No : ")

# setting variabel
harga = []
barang = []
total = 0
jumlah = []

a=int(input("Masukan Banyaknya Menu : "))
i = 0

for i in range (a):
    print("  Jenis Menu ke- ", i+1)
    KODE = int(input(" Masukkan Kode Barang : "))
    jumlah.append(int(input(" Jumlah Pesan: ")))
    
    
    if KODE == 1:
        barang.append("Mie Candu Tasty")
        harga.append(8500)
    elif KODE == 2:
        barang.append("Mie Jebew Spicy")
        harga.append(9000)
    elif KODE == 3:
        barang.append("Udang Kejuh")
        harga.append(10000)
    elif KODE == 4:
        barang.append("Siomay")
        harga.append(8000)
    elif KODE == 5:
        barang.append("Pangsit Goyeng")
        harga.append(9000)
    elif KODE == 6:
        barang.append("Telul Uyung")
        harga.append(7000)
    elif KODE == 7:
        barang.append("Mineral")
        harga.append(3000)
    elif KODE == 8:
        barang.append("Lemon Tea")
        harga.append(4000)
    elif KODE == 9:
        barang.append("Es Coklat")
        harga.append(5000)
    elif KODE == 10:
        barang.append("Es Jeruk")
        harga.append(5000)
    elif KODE == 11:
        barang.append("Teh Tarek")
        harga.append(6000)
    elif KODE == 12:
        barang.append("Mie Setan")
        harga.append(25000)
    else:
        print("Barang Tidak Terdaftar !!!")
        print("")
        break

# kalculator total harga
for i in range(len(harga)):
    total += harga[i] * jumlah[i]
    
print("")
print("")
print("==========================================================================")
print("                    =>  RESTO MIE JEBRET  <=")
print("                Jl. Raya Candi, Gondangsari, Clapar")
print("          Kec. Subah, Kabupaten Batang, Jawa Tengah 51262")
print("                   contact person : 083456719905")
print("--------------------------------------------------------------------------")
print("Waktu :", f_waktu)
print("Meja No :", mejo)
print("Nama Petugas : ", n_petugas)
print("==========================================================================")
print("  | No |      Nama Menu     |    Harga   | Jumlah Beli |  Total Bayar  |")
print("--------------------------------------------------------------------------")

# Print order item
for i in range(len(barang)):
   print(f"  | {i+1}  |   {barang[i]:<17}|  Rp {harga[i]:<7}|      {jumlah[i]}      |     Rp {harga[i] * jumlah[i]}  | ")

print("--------------------------------------------------------------------------")
print("                                              Total Harga = Rp.", total)
diskon = total - 0.20 * total
totaldiskon = total - diskon
if (total > 50000):
    print("                                         Total Diskon 20% = Rp.", totaldiskon)
    print("                                      Harga Bayar Menjadi = Rp.", diskon)
else :
    print("                                          Total Diskon 0% = Rp. 0")
    print("                                      Harga Bayar Menjadi = Rp.", total)

print("===========================================================================")

bayar=int(input("Masukan Uang yang di Bayar : "))
kembali1 = bayar - diskon
kembali2 = bayar - total
if (total >= 50000) :
    print("Uang Kembali Anda           : Rp. ", kembali1)
else :
    print("Uang Kembali Anda           : Rp. ", kembali2)

print("")
print("         ~ Jangan lupa datang lagi.. Terima Kasih....:) ~ ")
