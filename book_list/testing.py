import unittest
from .processing import BukuProcessor
from .validasi import cek_harga_valid, cek_data_kosong

class TestBuku(unittest.TestCase):
    def setUp(self):
        self.proc = BukuProcessor()
        # STATUS DISESUAIKAN LAGI
        self.data_dummy = [
            {'judul': 'Buku A', 'harga': 50000, 'status': 'Belum dibaca dan belum dibeli'},
            {'judul': 'Buku B', 'harga': 30000, 'status': 'Sudah dibaca dan sudah dibeli'}
        ]

    def test_hitung_total(self):
        self.assertEqual(self.proc.hitung_total_biaya(10, 20, 30), 60)

    def test_urutkan_buku(self):
        hasil = self.proc.urutkan_buku_termurah(self.data_dummy)
        self.assertEqual(hasil[0]['judul'], 'Buku B') 

    def test_filter_beli(self):
        hasil = self.proc.filter_wajib_beli(self.data_dummy)
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]['judul'], 'Buku A')

    def test_validasi_harga_negatif(self):
        with self.assertRaises(ValueError):
            cek_harga_valid(-1000)

    def test_validasi_data_kosong(self):
        with self.assertRaises(Exception):
            cek_data_kosong("", "")