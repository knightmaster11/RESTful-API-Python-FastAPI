from pydantic import BaseModel

class Barang(BaseModel):
    jenis: str
    kategori: str 
    kode_barang: str
    nama_barang: str
    style: str
    color: str
    size: str
    hs_code: str
    im: str
    satuan: str
    harga: str
    harga_pokok: str
    password: str
    currency: str
    status: str
    user_id: str
    keterangan: str
    selisih: str
    brand: str
    brutto: str
    netto: str
    type1: str
    type2: str
    pemasok: str
    type3: str