from email.errors import FirstHeaderLineIsContinuationDefect
from typing import Hashable
import datetime as dt
from urllib.request import AbstractHTTPHandler
hari_ini = dt.date.today()

print(50*"=")
print(13*"=", "Toko Kelontong Namiya",14*"=")
print(50*"=")
print("Harap isi data diri terlebih dahulu untuk melanjutkan!")
print("")
print(50*"-")
nama =   input("Nama lengkap                :")
alamat = input("Alamat tempat tinggal       :")
hp =     input("Nomor telepon               :")
print(50*"-")
print("Selamat datang di Toko Kelontong Namiya!")
print("Silahkan cari kebutuhan anda!")


kategori = input("Pilih Kategori[Alat Tulis/Makanan&Minuman]:")
if kategori == "alat tulis" or kategori == 'Alat Tulis' :
        kategori_barang = "alat tulis"
        jenisbarang = "Pensil 2B, Pulpen, Buku tulis"
        print(50*'-')
        print("Kategori               :", kategori_barang)
        print("Barang                 :", jenisbarang)
        print(50*'-')
        print("Barang                  Harga")
        print("1.Pensil 2B             Rp 1.000")
        print("2.Pulpen                Rp 2.000")
        print("3.Buku Tulis            Rp 5.000")
        print(50*'-')
elif kategori== "makanan&minuman" or kategori== "Makanan&Minuman" :
        kategori_barang = "Makanan & Minuman"
        jenisbarang = 'Kripik kentang, Kola, Permen karet'
        print(50*'-')
        print("Kategori               :", kategori_barang)
        print("Barang                 :", jenisbarang)
        print(50*'-')
        print("Barang                  Harga")
        print("4.Kripik Kentang        Rp 3.000")
        print("5.Kola                  Rp 5.000")
        print("6.Permen Karet          Rp 2.000")
        print(50*'-')
else: print("kategori tidak tersedia")
jumlah_beli = int(input('Masukan jumlah pembelian barang :'))
no_barang = []
nama_barang = []
jumlah_Pembelian =[]
total_belanja =[]
uang_bayar=[]
uang_kembali=[]
harga=[]
jumlah=[]
i=0
while i<jumlah_beli:
    print("Barang ke -", i+1)

    no_barang.append(int(input('Masukkan nomor barang  :')))
    jumlah_Pembelian.append(int(input('Masukkan jumlah pembelian  :')))
    if no_barang[i]== int(1):
        nama_barang.append('Pensil 2B')
        harga.append('1000')
        jumlah.append(jumlah_Pembelian[i]*int(1000))
    elif no_barang[i]== int(2):
        nama_barang.append('Pulpen')
        harga.append('2000')
        jumlah.append(jumlah_Pembelian[i]*int(2000))
    elif no_barang[i]== int(3):
        nama_barang.append('Buku Tulis')
        harga.append('5000')
        jumlah.append(jumlah_Pembelian[i]*int(5000))
    elif no_barang[i]== int(4):
        nama_barang.append('Kripik Kentang')
        harga.append('3000')
        jumlah.append(jumlah_Pembelian[i]*int(3000))
    elif no_barang[i]== int(5):
        nama_barang.append('Kola')
        harga.append('5000')
        jumlah.append(jumlah_Pembelian[i]*int(5000))
    elif no_barang[i]== int(6):
        nama_barang.append('Permen Karet')
        harga.append('2000')
        jumlah.append(jumlah_Pembelian[i]*int(2000))
    else : print('Tidak terdaftar')
    
    i =i+1
print("")    
print("")    
print('================================================')
print("                  Bon Pembelian            ")
print("              Toko Kelontong Namiya        ")
print(f"                    {hari_ini}")
print('================================================')
print('Nama    : ', nama)
print('Alamat  : ', alamat)
print('No telp : ', hp)
print('----------------------------------------------- ')
print("No  |  Qty  | Nama Barang  |  Harga  |  Jumlah  ")
total_belanja = 0
a = 0
while a < jumlah_beli:
    total_belanja = total_belanja + jumlah[a]
    print("%i       %i      %s      %s       %i"%(a+1, jumlah_Pembelian[a], nama_barang[a], harga[a], jumlah[a]))
    a = a+1
print('------------------------------------------------')
print('Total belanja     Rp.', total_belanja)
uang_bayar = int(input('Uang diterima     Rp. ',))
uang_kembali = uang_bayar - total_belanja
print('Uang kembali      Rp.', uang_kembali)
print('================================================' )
print('       Terima kasih telah berbelanja di'          )
print('            Toko Kelontong Namiya'                )
