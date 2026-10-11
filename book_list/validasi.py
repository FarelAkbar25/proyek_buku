def cek_harga_valid(harga):
    if harga < 0:
        raise ValueError("Harga tidak boleh negatif!")
    
    assert isinstance(harga, int), "Harga harus berupa angka bulat (integer)!"
    return True

def cek_data_kosong(judul, penulis):
    if not judul or not penulis:
        raise Exception("Judul dan Penulis buku tidak boleh kosong!")
    return True