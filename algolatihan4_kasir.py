#jumlah barang
miesedap = int(input("Jumlah Mie Sedap       :"))
minuman  = int(input("Jumlah Unjukan Suegerr :"))
tigan    = int(input("Jumlah Tigan           :"))
beras    = int(input("Jumlah Beras           :"))
lisah    = int(input("Jumlah lisah           :"))
gendhis  = int(input("Jumlah Gendhis         :"))

#regane
j_miesedap = 3000*miesedap
j_minuman  = 8000*minuman
j_tigan    = 15000*tigan
j_beras    = 12000*beras
j_lisah    = 14000*lisah
j_gendhis  = 10000*gendhis

#ngitung
belanja = (j_miesedap+j_minuman+j_tigan+j_beras+j_lisah+j_gendhis)

if (belanja >=100000) and (belanja < 200000):
    diskon = 10
    print('Wilujeng sampeyan lumangen diskon 10%')
elif (belanja >= 200000):
    diskon = 20
    print('Wilujeng sampeyan lumangen diskon 20%')
else:
  diskon = 0
  
# Total Harga 
harga = belanja - ((diskon/100)*belanja)


#output
print ("")
print ("")
print ("#######################################################")
print ("                    WARUNG SAINGAHA                    ")
print ("         Jl.Mberoh kae rt 6464 Kec.Sewidakrolas        ")
print ("-------------------------------------------------------")
import datetime 
waktu = datetime.datetime.now()
f_waktu = waktu.strftime("%A %x")
print(f_waktu,"~ltfh")
print ("#######################################################")
print (" No | Nama Barang | Qty |  Harga  |  Jumlah ")
print (" 1.   Mie Sedap     ",miesedap,    "   Rp.3000 ","", "Rp",j_miesedap)
print (" 2.   Minuman       ",minuman ,    "   Rp.8000 ","", "Rp",j_minuman)
print (" 3.   Tigan         ",tigan   ,  "   Rp.15000 ","","Rp",j_tigan)
print (" 4.   Beras         ",beras   ,  "   Rp.12000 ","","Rp",j_beras)
print (" 5.   Lisah         ",lisah   ,  "   Rp.14000 ","", "Rp",j_lisah)
print (" 6.   Gendhis       ",gendhis ,  "   Rp.10000 ","", "Rp",j_gendhis)
print ("")
print ("-------------------------------------------------------")
print ("                                Total Blonjo:Rp",belanja)
print ("                                Diskon(%)   :Rp",diskon)
print ("-------------------------------------------------------")
print ("Total mbayar  : Rp.",harga)

bayar=int(input("Jumlah Mbayare :Rp."))
sosok=(bayar-harga)
print("Pesanggrahan  :Rp.",sosok)

while bayar < harga:
    print ("Duete Kurang ora oleh Utang!!")
print ("#######################################################")
print ("                Ngaturaken Matur Nuwun                 ")
