import time
import os
from datetime 
import datetime

# Variabel global untuk menyimpan nama pengguna
nama_pengguna = ""

# Fungsi login untuk memasukkan nama pengguna
def login():
    global nama_pengguna
    nama_pengguna = input("Masukkan nama Anda: ")
    print(f"Selamat datang, {nama_pengguna}!")

# Fungsi untuk menampilkan animasi loading
def animasi_loading(pesan):
    print(pesan, end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()

# Fungsi untuk memuat jadwal dari file
def muat_jadwal(filename='jadwal.txt'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        lines = file.readlines()
    jadwal = []
    for line in lines:
        if line.strip():
            day, time, activity = line.strip().split('|')
            jadwal.append([day.strip(), time.strip(), activity.strip()])
    return jadwal

# Fungsi untuk menyimpan jadwal ke file
def simpan_jadwal(jadwal, filename='jadwal.txt'):
    with open(filename, 'w') as file:
        for item in jadwal:
            file.write(f"{item[0]} | {item[1]} | {item[2]}\n")

# Fungsi untuk menambahkan jadwal baru
def tambah_jadwal(jadwal):
    hari = input("Masukkan hari : ")
    waktu = input("Masukkan waktu : ")
    kegiatan = input("Masukkan kegiatan: ")
    jadwal.append([hari, waktu, kegiatan])
    simpan_jadwal(jadwal)
    print("Jadwal ditambahkan!")

# Fungsi untuk menampilkan jadwal
def tampilkan_jadwal(jadwal):
    if not jadwal:
        print("Tidak ada jadwal.")
    else:
        for idx, item in enumerate(jadwal, start=1):
            print(f"{idx}. {item[0]} | {item[1]} | {item[2]}")

# Fungsi untuk mengingatkan jadwal hari ini
def ingatkan_jadwal(jadwal):
    hari_ini = datetime.now().strftime("%A")
    print(f"Jadwal untuk hari ini ({hari_ini}):")
    ada_jadwal = False
    for item in jadwal:
        if item[0].lower() == hari_ini.lower():
            print(f"{item[1]} - {item[2]}")
            ada_jadwal = True
    if not ada_jadwal:
        print("Tidak ada jadwal untuk hari ini.")

# Fungsi untuk menghapus jadwal
def hapus_jadwal(jadwal):
    tampilkan_jadwal(jadwal)
    try:
        index = int(input("Masukkan nomor jadwal yang ingin dihapus: ")) - 1
        if 0 <= index < len(jadwal):
            del jadwal[index]
            simpan_jadwal(jadwal)
            print("Jadwal berhasil dihapus!")
        else:
            print("Nomor jadwal tidak valid.")
    except ValueError:
        print("Masukkan nomor yang valid.")

# Fungsi utama
def main():
    login()  # Meminta pengguna untuk login dan memasukkan nama

    jadwal = muat_jadwal()

    while True:
        print("\nAsisten Pribadi")
        print(f"Selamat datang, {nama_pengguna}!")
        print("1. Tambah Jadwal")
        print("2. Tampilkan Semua Jadwal")
        print("3. Ingatkan Jadwal Hari Ini")
        print("4. Hapus Jadwal")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih opsi: "))
            if pilihan == 1:
                tambah_jadwal(jadwal)
            elif pilihan == 2:
                tampilkan_jadwal(jadwal)
            elif pilihan == 3:
                animasi_loading("Mengecek jadwal")
                ingatkan_jadwal(jadwal)
            elif pilihan == 4:
                hapus_jadwal(jadwal)
            elif pilihan == 5:
                print(f"Terima kasih telah menggunakan your mini reminder, {nama_pengguna}(^_^)v")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Masukkan nomor yang valid.")

    # Keluar dari program
    exit()

main()
