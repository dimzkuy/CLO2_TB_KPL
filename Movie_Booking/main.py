from modules import auth, booking

def menu():
    print("\n=== Sistem Pemesanan Tiket ===")
    print("1. Daftar Akun")
    print("2. Login")
    print("3. Tampilkan Film")
    print("4. Pilih Film dan Jadwal")  
    print("5. Pilih Kursi")

    print("0. Keluar")

def daftar():
    username = input("Username baru: ")
    password = input("Password: ")
    try:
        auth.register(username, password)
        print("✅ Registrasi berhasil!")
    except Exception as e:
        print(f"❌ {e}")

def masuk():
    username = input("Username: ")
    password = input("Password: ")
    if auth.login(username, password):
        print("✅ Login berhasil!")
        return username
    else:
        print("❌ Login gagal.")
        return None

def tampilkan_film():
    films = booking.list_films()
    if not films:
        print("Belum ada film tersedia.")
    else:
        print("\n🎬 Daftar Film:")
        for f in films:
            print(f"- {f['id']}: {f['title']} ({f['schedule']})")

if __name__ == '__main__':
    while True:
        menu()
        choice = input("Pilih menu: ")
        if choice == '1':
            daftar()
            user = masuk()
        elif choice == '2':
            user = masuk()
        if user:
            judul_film, jadwal = booking.pilih_film_dan_jadwal()
            if judul_film and jadwal:
                kursi_terpilih = booking.pilih_kursi()
                if kursi_terpilih:
                    harga_per_kursi = 50000  # contoh harga tetap Rp50.000
                    if booking.proses_pembayaran(harga_per_kursi, len(kursi_terpilih)):
                        booking.simpan_transaksi(user, judul_film, jadwal, kursi_terpilih)
        elif choice == '3':
            booking.tampilkan_films()
        elif choice == '4':  # ✅ Tambahkan pilihan 4
            film, jadwal = booking.pilih_film_dan_jadwal()
            if film and jadwal:
                print(f"✅ Siap untuk lanjut pilih kursi di film '{film}' jam {jadwal}.")
        elif choice == '5':
            kursi_terpilih = booking.pilih_kursi()
            if kursi_terpilih:
                print(f"✅ Anda memilih kursi: {', '.join(kursi_terpilih)}")
            else:
                print("❌ Anda belum memilih kursi.")
        elif choice == '0':
            print("👋 Keluar dari sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
