import os

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def buat_file_awal(self):
        try:
            with open(self.filename, 'x') as f:
                # Menggunakan ljust dan garis tegak (|) agar persis seperti tabel
                f.write(f"{'Judul'.ljust(30)} | {'Penulis'.ljust(20)} | {'Harga'.ljust(10)} | Status\n")
        except FileExistsError:
            pass

    def tambah_buku(self, **kwargs):
        # Memotong teks jika terlalu panjang dan memberi spasi perataan (ljust)
        judul = str(kwargs.get('judul', 'Anonim'))[:30].ljust(30)
        penulis = str(kwargs.get('penulis', 'Anonim'))[:20].ljust(20)
        harga = str(kwargs.get('harga', 0)).ljust(10)
        status = kwargs.get('status', 'Belum dibaca dan belum dibeli')
        
        with open(self.filename, 'a') as f:
            # Menyimpan menggunakan garis tegak (|)
            f.write(f"{judul} | {penulis} | {harga} | {status}\n")

    def baca_buku(self):
        buku_list = []
        try:
            with open(self.filename, 'r') as f:
                next(f)  # Lewati header
                for baris in f:
                    # Membaca dan memotong berdasarkan garis tegak (|), lalu membersihkan spasi (strip)
                    data = [item.strip() for item in baris.strip().split('|')]
                    if len(data) == 4:
                        try:
                            harga = int(data[2])
                            buku_list.append({'judul': data[0], 'penulis': data[1], 'harga': harga, 'status': data[3]})
                        except ValueError:
                            pass # diam-diam melewati data rusak
        except FileNotFoundError:
            print(f"File {self.filename} belum ada.")
        return buku_list

    def tulis_laporan(self, data, nama_laporan, total_biaya=0):
        with open(nama_laporan, 'w') as f:
            f.write("LAPORAN DAFTAR BUKU WAJIB BELI:\n")
            
            if not data:
                f.write("Belum ada buku yang perlu dibeli.\n")
            else:
                for i, item in enumerate(data, 1):
                    f.write(f"{i}. Judul   : {item['judul']}\n")
                    f.write(f"   Penulis : {item['penulis']}\n")
                    f.write(f"   Harga   : Rp {item['harga']}\n")
                    f.write(f"   Status  : {item['status']}\n\n")
            
            f.write(f"Total buku wajib beli : {len(data)}\n")
            f.write(f"Total biaya disiapkan : Rp {total_biaya}\n")
            
        print(f"Laporan sudah di-generate ke file {nama_laporan}")