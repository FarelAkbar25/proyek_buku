import os
from book_list.fileio import FileHandler
from book_list.processing import BukuProcessor
from book_list.validasi import cek_harga_valid, cek_data_kosong

def main():
    fh = FileHandler("data_buku.txt")
    proc = BukuProcessor()
    fh.buat_file_awal()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        print("=== APLIKASI DAFTAR BUKU ===")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Buat Laporan Wajib Beli")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            print("\n-- Masukkan Data --")
            judul = input("Judul Buku: ")
            
            penulis = input("Penulis (kosongkan jika tidak tahu): ")
            if not penulis.strip():
                penulis = "Anonim"
                
            harga_input = input("Harga (Rp): ")
            
            print("Status Buku:")
            print("a. Belum dibaca dan belum dibeli")
            print("b. Sudah dibaca dan sudah dibeli")
            status_input = input("Pilih (a/b): ").lower()
            
            if status_input == 'b':
                status = "Sudah dibaca dan sudah dibeli"
            else:
                status = "Belum dibaca dan belum dibeli"
            
            try:
                harga = int(harga_input)
                if cek_data_kosong(judul, penulis) and cek_harga_valid(harga):
                    fh.tambah_buku(judul=judul, penulis=penulis, harga=harga, status=status)
                    print("Data berhasil disimpan!")
            except ValueError:
                print("Error: Harga harus berupa angka.")
            except Exception as e:
                print(f"Error: {e}")
                
            input("\nTekan Enter untuk lanjut...")
                
        elif pilihan == '2':
            print("\n-- Semua Daftar Buku --\n")
            data_buku = fh.baca_buku()
            if not data_buku:
                print("Data masih kosong.")
            else:
                for idx, b in enumerate(data_buku, 1):
                    print(f"{idx}. Judul   : {b['judul']}")
                    print(f"   Penulis : {b['penulis']}")
                    print(f"   Harga   : Rp {b['harga']}")
                    print(f"   Status  : {b['status']}")
                    print()
            
            input("Tekan Enter untuk lanjut...")
                    
        elif pilihan == '3':
            print("\n-- Proses Laporan --")
            data_buku = fh.baca_buku()
            if not data_buku:
                print("Data kosong.")
            else:
                buku_wajib_beli = proc.filter_wajib_beli(data_buku)
                harga_wajib_beli = [b['harga'] for b in buku_wajib_beli]
                
                total_biaya = proc.hitung_total_biaya(*harga_wajib_beli) if harga_wajib_beli else 0
                
                print(f"Buku yang harus dibeli: {len(buku_wajib_beli)}")
                print(f"Total biaya: Rp {total_biaya}")
                
                fh.tulis_laporan(buku_wajib_beli, "laporan_buku.txt", total_biaya)
            
            input("\nTekan Enter untuk lanjut...")
            
        elif pilihan == '4':
            print("Program selesai.")
            break
            
        else:
            print("Pilihan salah.")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()