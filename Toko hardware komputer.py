import os
os.system("cls")

from prettytable import PrettyTable

# Data dari Produk yang diperjualkan oleh toko
dataProduk = [
    [1, "Processor (Intel Core i7-12700)", 5000000],
    [2, "Processor (AMD Ryzen 5 3600)", 3300000],
    [3, "RAM (Corsair Vengeance 32GB DDR4 3200Mhz)", 1430000],
    [4, "RAM (Corsair Vengeance 16GB DDR4 2666MHz)", 700000],
    [5, "RAM (Corsair Vengeance LPX 16GB DDR4 3300MHz)", 750000],
    [6, "Motherboard (MSI B450 Tomahawk Max)", 2000000],
    [7, "Motherboard (ASUS ROG Maximus Z690 Extreme Glacial DDR5)", 35000000],
    [8, "Motherboard (MSI PRO Z690-A DDR4 ProSeries)", 1200000],
    [9, "SSD (Samsung 960 PRO NVMe M.2 512GB)", 4500000],
    [10, "SSD (Western Digital Blue SN550 NVMe 1TB)", 2300000]
]

# Untuk menyimpan produk yang dibeli oleh buyer/pembeli
produkDibeli = []

# Create
def bikinBaru() :
    munculkan()
    nomor = int(input('Masukan Nomor barang yang baru : '))

    # Mengecek apakah angka nya sudah ada list apa belum
    for angkaProduk in dataProduk:
        if angkaProduk[0] == nomor:
            print(f'Produk dengan nomor {nomor} sudah ada.')
            return

    namaBarang = str(input('\nMasukkan Nama Barang : '))
    hargaBarang = int(input('Masukkan Harga Barang : '))
    dataProduk.append([nomor, namaBarang, hargaBarang])
    munculkan()
    print('\nProduk baru berhasil ditambahkan')

# Read
def munculkan() :
    tabelDataProduk = PrettyTable(['No.', 'Nama Barang', 'Harga Barang'])
    for barisData in dataProduk :
        tabelDataProduk.add_row(barisData)

    print(tabelDataProduk)

# Update
def perbaharui() :
    munculkan()
    noBaru = int(input('Masukan nomor yang ingin di update : '))
    for barisData in dataProduk :

        if barisData [0] == noBaru :
            namaBaru = str(input('Masukkan Nama Barang yang baru : '))
            hargaBaru = int(input('Masukkan Harga Barang yang baru : '))
            barisData[1] = namaBaru
            barisData[2] = hargaBaru
            munculkan()
            print('Produk berhasil diperbarui')
            return
    print('Nomor barang tidak ditemukan')

# Delete
def hapuskan() :
    munculkan()
    noHapus = int(input('Masukan nomor yang ingin dihapus: '))
    for barisData in dataProduk:
        if barisData[0] == noHapus:
            dataProduk.remove(barisData)
            munculkan()
            print('Produk berhasil dihapus')
            return
    print('Nomor barang tidak ditemukan')

# Proses Transaksi
def prosesTransaksi():
    while True :
        munculkan()
        noProduk = int(input('Masukkan nomor produk yang ingin dibeli (Masukan "000" untuk selesai): '))
        if noProduk == 000:
            break
        
        for barisData in dataProduk:
            if barisData[0] == noProduk:
                jumlahPembelian = int(input('Masukkan jumlah yang ingin dibeli : '))
                totalHarga = barisData[2] * jumlahPembelian
                produkDibeli.append([barisData[0], barisData[1], jumlahPembelian, totalHarga])
                print(f'{barisData[1]} ({jumlahPembelian} pcs) telah ditambahkan ke keranjang.')

    print('\nTabel Transaksi')
    tabelProsesTransaksi = PrettyTable(['No.', 'Nama Produk', 'Jumlah Beli', 'Total Harga'])
    totalHargaBelanja = 0
    for barisBeli in produkDibeli:
        tabelProsesTransaksi.add_row(barisBeli)
        totalHargaBelanja += barisBeli[3]
    print(tabelProsesTransaksi)
    print(f'Total Belanja Anda: {totalHargaBelanja}')

# Login Admin
def loginAdmin() :
    while True :
        username = input("Masukan Username admin : ")
        password = input("Masukan password : ")

        if username == "Iqbal" :
            if password == "abc" :
                print("Selamat Datang Iqbal")
                menuAdmin()
                break
            else :
                (print("Login gagal, coba lagi"))
        else :
            (print("Login gagal, coba lagi"))

# Menu admin
def menuAdmin() :
    while True :
        print("\nMenu Admin:")
        print("1. Tampilkan Produk")
        print("2. Tambah Produk Baru")
        print("3. Perbarui Produk")
        print("4. Hapus Produk")
        print("5. Keluar")
        
        pilihan_admin = int(input("Pilih aksi yang ingin dilakukan (1/2/3/4/5): "))

        if pilihan_admin == 1:
            munculkan()
        elif pilihan_admin == 2:
            bikinBaru()
        elif pilihan_admin == 3:
            perbaharui()
        elif pilihan_admin == 4:
            hapuskan()
        elif pilihan_admin == 5:
            break
        else :
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Pemilihan role
def role() :
    while True :
        pilihPeran = str(input('Apakah anda ingin menjadi admin atau pembeli ?\n'))
        if pilihPeran == 'admin' :
            loginAdmin()
            break
        elif pilihPeran == 'pembeli':
            prosesTransaksi()
            break
        else :
            print('Pilihan tidak valid, silahkan pilih antara admin atau pembeli')

role()
