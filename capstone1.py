#Rental Mobil

from tabulate import tabulate

# 1. MEMBUAT DAFTAR MOBIL 
mobil_list = [
    {"ID": 'E1', "Jenis": "Hiace", "Transmisi": "MT", "Harga": 500000, "Kapasitas": 11, "Stok": 5},
    {"ID": 'J2', "Jenis": "Jazz", "Transmisi": "AT", "Harga": 400000, "Kapasitas": 4, "Stok": 3},
    {"ID": 'A3', "Jenis": "Agya", "Transmisi": "AT", "Harga": 350000, "Kapasitas": 3, "Stok": 4},
    {"ID": 'B4', "Jenis": "Brio", "Transmisi": "MT", "Harga": 300000, "Kapasitas": 3, "Stok": 7},
    {"ID": 'E5', "Jenis": "Ertiga", "Transmisi": "AT", "Harga": 350000, "Kapasitas": 6, "Stok": 4},
    {"ID": 'E6', "Jenis": "Elf", "Transmisi": "MT", "Harga": 450000, "Kapasitas": 11, "Stok": 5}]

transaksi = []
recycle_bin = []

# FUNGSI PILIHAN TRANSMISI
def transmisi():
    while True:
        transmisi_baru = validasi_alfabet('Masukkan Transmisi (AT/MT): ').upper().strip()
        if transmisi_baru in ['AT', 'MT']:
            return transmisi_baru  # Keluar dari loop jika input valid
        print('\nMasukkan data yang valid! (AT atau MT)') 

# FUNGSI RANDOM ANGKA
import random
def generate_angka(jenis):

    if mobil_list:  # Cek apakah mobil_list tidak kosong
        angka_terakhir = max(int(mobil["ID"][1:]) for mobil in mobil_list)  # Ambil angka terbesar dari ID
    else:
        angka_terakhir = 0
    angka_baru = angka_terakhir + 1  # Tambahkan 1 ke angka terakhir
    huruf_pertama = jenis[0].upper()  # Ambil huruf pertama dari nama jenis mobil
    hasil = f'{huruf_pertama}{angka_baru}'  # Format ID baru
    return hasil

#FUNGSI PILIHAN LANJUT YA/TIDAK
def lanjutkan(callback):
    while True:
        masih_pesanan = validasi_alfabet('Ada lagi? (Ya/Tidak): ').capitalize()
        if masih_pesanan == 'Ya':
            callback()
            break
        elif masih_pesanan == 'Tidak':
            menu_utama()
            break
        else:
            print("\nMasukan Ya dan Tidak Saja!\n")
# 2. Membaca Tabulasi (READ)
def read_mobil():
    print("\n=== Daftar Rental Mobil Kami ===")
    print(tabulate(mobil_list, headers='keys', tablefmt='fancy_grid')) #menunjukan tabel stok
    print(' ')
def transaksi_mobil():
    print("\n           === Booked! ===")
    print(tabulate(transaksi, headers='keys', tablefmt='fancy_grid')) #menunjukan tabel transaksi
def tong_sampah():
    print("           === Recycle Bin! ===")
    print(tabulate(recycle_bin, headers='keys', tablefmt='fancy_grid')) #menunjukan tabel transaksi

# 3. Membuat Fungsi validasi input
def validasi_alfabet(prompt): #validasi untuk input huruf
    while True:
        inputan = input(prompt).strip().replace(" ","")
        if inputan.isalpha():
            return inputan
        else:
            print("\nInputan harus berupa huruf!")
def validasi_angka(prompt): #validasi untuk input angka
    while True:
        inputan = input(prompt).strip()
        if inputan.isdigit():
            return int(inputan)
        else:
            print("\nInputan harus berupa angka!")

# 4. Isi info kendaraan baru (CREATE)
def info():
    while True:
        jenis_baru = validasi_alfabet('Masukan Mobil Baru: ').capitalize()
        no_baru = generate_angka(jenis_baru) #menambah otomatis No. pada tabel
        transmisi_new = transmisi()
        harga_baru = validasi_angka('Masukan Harganya: ')
        kapasitas_baru = validasi_angka('Masukan Kapasitas Mobilnya: ')
        stok_baru = validasi_angka('Masukan Stoknya: ')
        mobil_baru = {"ID": no_baru, "Jenis": jenis_baru, "Transmisi": transmisi_new, "Harga": harga_baru, "Kapasitas": kapasitas_baru, "Stok": stok_baru}
        
        mobil_list.append(mobil_baru) #menambah inputan kedalam list dict
        return read_mobil() #kembali menunjukan list tabel terbaru

# 5. Mengupdate stok yang ada (UPDATE)
def update_stok():
    update_tabel = input('\nMasukan ID. Mobil yang ingin diupdate (Ketik 0 Jika Batal): ').capitalize().strip()
    if update_tabel == '0':
        return
    elif update_tabel not in [mobil['ID'] for mobil in mobil_list]:
        print ('\nData tidak ditemukan! Masukan data yang Valid')
        return update_stok()
    
    
    #Checking data yang diupdate
    for item in mobil_list:
        if item ['ID'] == update_tabel:
            while True:
                update = validasi_alfabet('\nMasukan data yang ingin diperbarui (Jenis/Harga/Transmisi/Kapasitas/Stok): ').capitalize()
                if update == 'Jenis':
                    item['Jenis'] = validasi_alfabet('Masukan Jenis Mobil Baru: ').capitalize()
                    item['ID'] = generate_angka(item['Jenis'])
                elif update == 'Transmisi':
                    item['Transmisi'] = transmisi()
                elif update == 'Harga':
                    item['Harga'] = validasi_angka('Masukan Harga Baru: ')
                elif update == 'Kapasitas':
                    item['Kapasitas'] = validasi_angka('Masukan Kapasitas Baru: ')
                elif update == 'Stok':
                    item['Stok'] = validasi_angka('Masukan Stok Baru: ')
                else:
                    print('\nData tidak ditemukan. Masukan data yang Valid')
                    continue
                
                lanjutkan(update_stok)
                break

# 6. Menghapus data yang sudah ada (DELETE)
def hapus_data():
    hapus_tabel = input('\nMasukan ID. Mobil yang ingin dihapus (Ketik 0 Jika Batal): ').capitalize()
    if hapus_tabel == '0':
        return
    elif hapus_tabel not in [mobil['ID'] for mobil in mobil_list]:
        print ('\nData tidak ditemukan! Masukan data yang Valid')
        return hapus_data()
        
    for item in mobil_list:
        if item['ID'] == hapus_tabel:
            mobil_list.remove(item)
            recycle_bin.append(item)
            print('\n                          Data berhasil dihapus')
            read_mobil()
            break
           
    else:
        return print("\nMobil tidak ditemukan! Kembali ke menu.")

# 7. Menambah data Transaksi (ADDED FEATURE)
# Fungsi Sortir Mobil
def filter_mobil():
    while True:
        print("\n=== Filter Mobil ===")
        print(' ')
        print("1. Urutkan berdasarkan Harga")
        print("2. Filter berdasarkan Jenis Transmisi")
        print("3. Urutkan berdasarkan Kapasitas")
        print("4. Kembali ke Menu Utama")
        print(' ')
        
        pilihan = validasi_angka("Pilih filter (1/2/3/4): ")
        
        # Urutkan berdasarkan harga
        if pilihan == 1:
            sort_order = validasi_alfabet("\nUrutkan harga dari rendah ke tinggi atau tinggi ke rendah? (rendah/tinggi): ").lower().strip()
            if sort_order == "rendah":
                sorted_mobil = sorted(mobil_list, key=lambda x: x["Harga"])
            elif sort_order == "tinggi":
                sorted_mobil = sorted(mobil_list, key=lambda x: x["Harga"], reverse=True)
            else:
                print("\nInput tidak valid!")
                continue
            
            print("\n=== Hasil Filter Harga ===")
            print(tabulate(sorted_mobil, headers="keys", tablefmt="fancy_grid"))

        # Filter berdasarkan transmisi
        elif pilihan == 2:
            transmisi_filter = validasi_alfabet("\nMasukkan jenis transmisi yang dicari (AT/MT): ").upper().strip()
            if transmisi_filter not in ["AT", "MT"]:
                print("\nInput tidak valid! Pilih AT atau MT.")
                continue
            
            filtered_mobil = [mobil for mobil in mobil_list if mobil["Transmisi"].strip() == transmisi_filter]
            
            print(f"\n=== Mobil dengan Transmisi {transmisi_filter} ===")
            print(tabulate(filtered_mobil, headers="keys", tablefmt="fancy_grid"))

        # Urutkan berdasarkan kapasitas
        elif pilihan == 3:
            sort_order = validasi_alfabet("\nUrutkan kapasitas dari kecil ke besar atau besar ke kecil? (kecil/besar): ").lower().strip()
            if sort_order == "kecil":
                sorted_mobil = sorted(mobil_list, key=lambda x: x["Kapasitas"])
            elif sort_order == "besar":
                sorted_mobil = sorted(mobil_list, key=lambda x: x["Kapasitas"], reverse=True)
            else:
                print("\nInput tidak valid!")
                continue

            print("\n=== Hasil Filter Kapasitas ===")
            print(tabulate(sorted_mobil, headers="keys", tablefmt="fancy_grid"))

        # Kembali ke menu utama
        elif pilihan == 4:
            return
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")
print(' ')


# FUNGSI BOOKING/TAMBAH TRANSAKSI
def tambah_transaksi():
    read_mobil()
    pesanan = input('\nMasukan ID. Mobil yang ingin disewa (Ketik 0 untuk batal): ').capitalize()
    if pesanan == "0":
        return
    elif pesanan not in [mobil['ID'] for mobil in mobil_list]:
        print ('\nData tidak ditemukan! Masukan data yang Valid\n')
        return tambah_transaksi()
    
    for mobil in mobil_list:
        if pesanan in [mobil['ID'] for mobil in mobil_list]:
            if mobil['ID'] == pesanan:
                jumlah = validasi_angka("Masukkan jumlah yang ingin disewa: ")
                if mobil['Stok'] >= jumlah:
                    mobil['Stok'] -= jumlah
                    transaksi.append({"ID.": pesanan,
                                       "Jenis": mobil['Jenis'],
                                         "Transmisi" : mobil['Transmisi'],
                                           "Harga": mobil['Harga'],
                                             "Jumlah": jumlah,
                                               "Total": mobil['Harga']*jumlah})
                    print(f"\n=== Berhasil menyewa {jumlah} unit {mobil['Jenis']}! ===")
                    transaksi_mobil()
                else:
                    print("\nStok tidak mencukupi!\n")
                    return tambah_transaksi()
                
                lanjutkan(tambah_transaksi)
                break  
        
            
# 8. Menu utama untuk memilih (MENU)
def menu_utama():
    while True:
        print('\n--- 𝐖 𝐄 𝐋 𝐂 𝐎 𝐌 𝐄 ---')
        print("\n=== Menu Administrasi ===\n")
        print("1. Lihat Daftar Mobil")
        print("2. Isi Daftar Kendaraan Baru")
        print("3. Update Tabel")
        print("4. Hapus Data")
        print("5. Tampilkan Recyle Bin")
        print("6. Booking Mobil")
        print("7. Filter Mobil")
        print("8. Keluar")
        print(' ')
        pilihan = validasi_angka("Pilih menu (1/2/3/4/5/6/7/8): ")
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
            tong_sampah()
        elif pilihan == 6:
            tambah_transaksi()
        elif pilihan == 7:
            filter_mobil()
        else:
            print("\n================= Terima kasih! =================\n")
            break 
menu_utama()