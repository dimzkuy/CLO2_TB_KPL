import json
import os

FILMS_FILE = 'Movie_Booking/data/films.json'

def list_films():
    if not os.path.exists(FILMS_FILE):
        print(f"⚠️ File {FILMS_FILE} tidak ditemukan!")  # Debug
        return []
    with open(FILMS_FILE, 'r') as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            print("❌ Format JSON films.json error!")
            return []

def tampilkan_films():
    films = list_films()
    if not films:
        print("Belum ada film yang tersedia.")
        return

    print("\n=== Daftar Film ===")
    for film in films:
        print(f"{film['id']}. {film['judul']}")
        print("   Jadwal: ", ", ".join(film['jadwal']))


def pilih_film_dan_jadwal():
    films = list_films()
    if not films:
        print("Belum ada film tersedia.")
        return None, None

    print("\n=== Pilih Film ===")
    for film in films:
        print(f"{film['id']}. {film['judul']}")

    while True:
        try:
            id_film = int(input("Masukkan ID Film yang ingin ditonton: "))
            film_terpilih = next((film for film in films if film['id'] == id_film), None)
            if film_terpilih:
                break
            else:
                print("❌ ID Film tidak valid. Coba lagi.")
        except ValueError:
            print("❌ Input harus angka.")

    print(f"\nJadwal tersedia untuk {film_terpilih['judul']}:")
    for idx, jam in enumerate(film_terpilih['jadwal']):
        print(f"{idx+1}. {jam}")

    while True:
        try:
            pilihan_jadwal = int(input("Pilih nomor jadwal: "))
            if 1 <= pilihan_jadwal <= len(film_terpilih['jadwal']):
                jadwal_dipilih = film_terpilih['jadwal'][pilihan_jadwal-1]
                break
            else:
                print("❌ Pilihan jadwal tidak tersedia.")
        except ValueError:
            print("❌ Input harus angka.")

    print(f"\n🎟️ Anda memilih film '{film_terpilih['judul']}' pada pukul {jadwal_dipilih}.")
    return film_terpilih['judul'], jadwal_dipilih


def tampilkan_kursi(grid_kursi):
    print("\n=== Layout Kursi ===")
    for baris in grid_kursi:
        print(" ".join(baris))

def pilih_kursi():
    # Buat grid kursi awal
    grid_kursi = [
        ["A1", "A2", "A3", "A4", "A5"],
        ["B1", "B2", "B3", "B4", "B5"],
        ["C1", "C2", "C3", "C4", "C5"]
    ]

    tampilkan_kursi(grid_kursi)

    pilihan = []
    while True:
        kursi = input("Masukkan kode kursi yang ingin dipesan (contoh A1), atau ketik 'selesai' untuk selesai: ").upper()
        if kursi == 'SELESAI':
            break

        # Cari dan booking kursi
        found = False
        for i in range(len(grid_kursi)):
            for j in range(len(grid_kursi[i])):
                if grid_kursi[i][j] == kursi:
                    grid_kursi[i][j] = "XX"  # tandai kursi sudah dipesan
                    pilihan.append(kursi)
                    found = True
                    print(f"✅ Kursi {kursi} berhasil dipesan.")
                    break
            if found:
                break
        if not found:
            print("❌ Kursi tidak tersedia atau sudah dipesan. Coba lagi.")

        tampilkan_kursi(grid_kursi)

    return pilihan

TRANSACTIONS_FILE = 'Movie_Booking/data/transactions.json'

def simpan_transaksi(username, judul_film, jadwal, kursi_terpilih):
    transaksi = {
        'username': username,
        'film': judul_film,
        'jadwal': jadwal,
        'kursi': kursi_terpilih
    }

    # Load transaksi lama
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(transaksi)

    # Simpan transaksi baru
    with open(TRANSACTIONS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    print("✅ Transaksi berhasil disimpan!")

def proses_pembayaran(harga_per_kursi, jumlah_kursi):
    total = harga_per_kursi * jumlah_kursi
    print(f"\n💵 Total yang harus dibayar: Rp {total:,}")

    while True:
        try:
            bayar = int(input("Masukkan jumlah pembayaran: Rp "))
            if bayar >= total:
                kembalian = bayar - total
                print(f"✅ Pembayaran berhasil! Kembalian Anda: Rp {kembalian:,}")
                return True
            else:
                print("❌ Uang Anda kurang. Coba lagi.")
        except ValueError:
            print("❌ Input harus berupa angka.")

