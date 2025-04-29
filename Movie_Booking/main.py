from modules import auth, booking
from modules.report.csv_exporter import CSVExporter
from modules.report.pdf_exporter import PDFExporter
import json
import os

def menu():
    print("\n=== Sistem Pemesanan Tiket ===")
    print("1. Daftar Akun")
    print("2. Login")
    print("3. Tampilkan Film")
    print("4. Pilih Film dan Jadwal")
    print("5. Pilih Kursi")
    print("6. Export Transaksi (csv/pdf)")  # Fitur baru
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

def export_transaction_data():
    path = "data/transactions.json"
    if not os.path.exists(path):
        print("❌ Data transaksi tidak ditemukan.")
        return

    with open(path) as f:
        transactions = json.load(f)

    if not transactions:
        print("❌ Belum ada transaksi.")
        return

    print("Export format? (csv/pdf): ", end="")
    format = input().lower()

    if format == "csv":
        exporter = CSVExporter()
        filename = "data/transactions_export.csv"
    elif format == "pdf":
        exporter = PDFExporter()
        filename = "data/transactions_export.pdf"
    else:
        print("❌ Format tidak dikenali.")
        return

    exporter.export(transactions, filename)

if __name__ == '__main__':
    user = None
    while True:
        menu()
        choice = input("Pilih menu: ")

        if choice == '1':
            daftar()
            user = None
            continue
        elif choice == '2':
            user = masuk()
        elif choice == '3':
            booking.tampilkan_films()
        elif choice == '4':
            if user:
                film, jadwal = booking.pilih_film_dan_jadwal()
                if film and jadwal:
                    print(f"✅ Siap untuk lanjut pilih kursi di film '{film}' jam {jadwal}.")
            else:
                print("❌ Anda harus login terlebih dahulu.")
        elif choice == '5':
            if user:
                kursi_terpilih = booking.pilih_kursi()
                if kursi_terpilih:
                    print(f"✅ Anda memilih kursi: {', '.join(kursi_terpilih)}")
                else:
                    print("❌ Anda belum memilih kursi.")
            else:
                print("❌ Anda harus login terlebih dahulu.")
        elif choice == '6':
            export_transaction_data()
        elif choice == '0':
            print("👋 Keluar dari sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
