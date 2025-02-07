#Rental Mobil

from tabulate import tabulate

# 1. Membuat stok mobil
mobil_list = [
    {"No": 1, "Jenis": "Hiace", "Harga": 500000, "Kapasitas": 5, "Stok": 5},
    {"No": 2, "Jenis": "Jazz", "Harga": 400000, "Kapasitas": 4, "Stok": 3},
    {"No": 3, "Jenis": "Agya", "Harga": 350000, "Kapasitas": 3, "Stok": 4}]

transaksi = []

# 2. Membaca mobil_list (READ)
def read_mobil():
    print("=== Daftar Rental Mobil Kami ===")
    print(tabulate(mobil_list, headers='keys', tablefmt='fancy_grid')) #menunjukan tabel stok
    print(' ')
def transaksi_mobil():
    print("           === Booked! ===")
    print(tabulate(transaksi, headers='keys', tablefmt='fancy_grid')) #menunjukan tabel transaksi

# 3. Membuat validasi input
def validasi_alfabet(prompt): #validasi untuk input huruf
    while True:
        inputan = input(prompt)
        if inputan.isalpha():
            return inputan
        else:
            print("Inputan harus berupa huruf!")

def validasi_angka(prompt): #validasi untuk input angka
    while True:
        inputan = input(prompt)
        if inputan.isdigit():
            return int(inputan)
        else:
            print("Inputan harus berupa angka!")

# 4. Isi info kendaraan baru (CREATE)
def info():
    while True:
        no_baru = len(mobil_list) + 1 #menambah otomatis No. pada tabel
        jenis_baru = validasi_alfabet('Masukan Mobil Baru: ').capitalize()
        harga_baru = validasi_angka('Masukan Harganya: ')
        kapasitas_baru = validasi_angka('Masukan Kapasitas Mobilnya: ')
        stok_baru = validasi_angka('Masukan Stoknya: ')
        mobil_baru = {"No": no_baru, "Jenis": jenis_baru, "Harga": harga_baru, "Kapasitas": kapasitas_baru, "Stok": stok_baru}
        mobil_list.append(mobil_baru) #menambah inputan kedalam list dict
        return read_mobil #kembali menunjukan list tabel terbaru

# 5. Mengupdate stok yang ada (UPDATE)

def update_stok():
    update_tabel = validasi_angka('Masukan No. Mobil yang ingin diupdate (Ketik 0 Jika Batal): ')
    if update_tabel == 0:
        return 
    #Checking data yang diupdate
    for item in mobil_list:
        if item ['No'] == update_tabel:
            while True:
                update = validasi_alfabet('Masukan data yang ingin diperbarui (Jenis/Harga/Kapasitas/Stok): ').capitalize()
                if update == 'Jenis':
                    item['Jenis'] = validasi_alfabet('Masukan Jenis Mobil Baru: ').capitalize()
                elif update == 'Harga':
                    item['Harga'] = validasi_angka('Masukan Harga Baru: ')
                elif update == 'Kapasitas':
                    item['Kapasitas'] = validasi_angka('Masukan Kapasitas Baru: ')
                elif update == 'Stok':
                    item['Stok'] = validasi_angka('Masukan Stok Baru: ')
                else:
                    print('Data tidak ditemukan. Masukan data yang Valid')
                
                masih_update = validasi_alfabet('Ada lagi? (Ya/Tidak): ').capitalize()
                if masih_update != 'Ya':
                    read_mobil()
                    break
                print('Data berhasil Diperbarui')

# 6. Menghapus data yang sudah ada (DELETE)
def hapus_data():
    hapus_tabel = validasi_angka('Masukan No. Mobil yang ingin dihapus (Ketik 0 Jika Batal): ')
    if hapus_tabel == 0:
        return
        
    for item in mobil_list:
        if item['No'] == hapus_tabel:
            mobil_list.remove(item)
            print('Data berhasil dihapus')
            read_mobil()
            break

# 7. Menambah data Transaksi (ADDED FEATURE)
def tambah_transaksi():
    read_mobil()
    pesanan = validasi_angka('Masukan No. Mobil yang ingin disewa: ')
    jumlah = validasi_angka("Masukkan jumlah yang ingin disewa: ")
    for mobil in mobil_list:
        if pesanan in [mobil['No'] for mobil in mobil_list]:
            if mobil['No'] == pesanan:
                if mobil['Stok'] >= jumlah:
                    mobil['Stok'] -= jumlah
                    transaksi.append({"No.": pesanan, "Jenis": mobil['Jenis'], "Harga": mobil['Harga'], "Jumlah": jumlah, "Total": mobil['Harga']*jumlah})
                    print(' ')
                    print(f"=== Berhasil menyewa {jumlah} unit {mobil['Jenis']}! ===")
                    return transaksi_mobil()
                else:
                    print("Stok tidak mencukupi!\n")
        else:
            print("Mobil tidak ditemukan!\n")
        
            
# 8. Menu utama untuk memilih
def menu_utama():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat Daftar Mobil")
        print("2. Isi Info Kendaraan Baru")
        print("3. Update Tabel")
        print("4. Hapus Data")
        print("5. Booking Mobil")
        print("6. Keluar")
        print(' ')
        pilihan = validasi_angka("Pilih menu (1/2/3/4/5/6): ")
        if pilihan == 1:
            read_mobil()
        elif pilihan == 2:
            info()
        elif pilihan == 3:
            read_mobil()
            update_stok()
        elif pilihan == 4:
            read_mobil()
            hapus_data()
        elif pilihan == 5:
            tambah_transaksi()
        else:
            print("Terima kasih!")
            break


menu_utama()