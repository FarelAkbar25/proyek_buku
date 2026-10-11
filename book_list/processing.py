class BukuProcessor:
    def hitung_total_biaya(self, *args):
        return sum(args)
    
    def urutkan_buku_termurah(self, buku_list):
        return sorted(buku_list, key=lambda x: x['harga'])
    
    def filter_wajib_beli(self, buku_list):
        return list(filter(lambda x: x['status'] == 'Belum dibaca dan belum dibeli', buku_list))