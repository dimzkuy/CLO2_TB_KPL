from modules import auth, booking
from modules.report.csv_exporter import CSVExporter
import json
import os

def menu():
    print("\n=== Sistem Pemesanan Tiket ===")
    print("1. Daftar Akun")
    print("2. Login")
    print("3. Tampilkan Film")
    print("4. Pilih Film dan Jadwal")
    print("5. Pilih Kursi")
    print("6. Export Transaksi (csv)")
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

def export_transaction_data():
    path = "Movie_Booking/data/transactions.json"
    if not os.path.exists(path):
        print("❌ Data transaksi tidak ditemukan.")
        return

    with open(path) as f:
        transactions = json.load(f)

    if not transactions:
        print("❌ Belum ada transaksi.")
        return

    # Ambil hanya transaksi terakhir
    last_transaction = transactions[-1:]

    format = input("Export format? (csv): ").strip().lower()
    os.makedirs("data", exist_ok=True)

    if format in ["csv", "ya"]:
        exporter = CSVExporter()
        filename = "data/last_transaction_export.csv"
        exporter.export(last_transaction, filename)
        print("✅ Transaksi terakhir berhasil diekspor ke", filename)
    else:
        print("❌ Format tidak dikenali.")


# ==============================
#        MAIN PROGRAM (FSM)
# ==============================
if __name__ == '__main__':
    user = None
    film = None
    jadwal = None
    current_state = "NOT_LOGGED_IN"  # Initial state

    while True:
        menu()
        choice = input("Pilih menu: ")

        if choice == '1':
            daftar()
            current_state = "NOT_LOGGED_IN"

        elif choice == '2':
            user = masuk()
            if user:
                current_state = "LOGGED_IN"
            else:
                current_state = "NOT_LOGGED_IN"

        elif choice == '3':
            booking.tampilkan_films()

        elif choice == '4':
            if current_state == "LOGGED_IN":
                film, jadwal = booking.pilih_film_dan_jadwal()
                if film and jadwal:
                    current_state = "FILM_SELECTED"
                    print(f"✅ Siap lanjut pilih kursi di '{film}' jam {jadwal}.")
            else:
                print("❌ Anda harus login terlebih dahulu.")

        elif choice == '5':
            if current_state == "FILM_SELECTED":
                kursi_terpilih = booking.pilih_kursi()
                if kursi_terpilih:
                    print(f"✅ Anda memilih kursi: {', '.join(kursi_terpilih)}")
                    booking.simpan_transaksi(user, film, jadwal, kursi_terpilih)
                    current_state = "LOGGED_IN"  # Kembali ke state sebelumnya
                else:
                    print("❌ Anda belum memilih kursi.")
            elif current_state == "LOGGED_IN":
                print("❌ Silakan pilih film dan jadwal terlebih dahulu (menu 4).")
            else:
                print("❌ Anda harus login terlebih dahulu.")

        elif choice == '6':
            export_transaction_data()

        elif choice == '0':
            print("👋 Keluar dari sistem. Sampai jumpa!")
            break

        else:
            print("❌ Pilihan tidak valid.")
