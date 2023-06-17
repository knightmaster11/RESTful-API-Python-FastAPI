from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

barangs = Table(
    'barangs',meta,
    Column('id',Integer,primary_key=True),
    Column('jenis',String(225)),
    Column('kategori',String(225)),
    Column('kode_barang',String(225)),
    Column('nama_barang',String(225)),
    Column('style',String(225)),
    Column('color',String(225)),
    Column('size',String(225)),
    Column('hs_code',String(225)),
    Column('im',String(225)),
    Column('satuan',String(225)),
    Column('harga',String(225)),
    Column('harga_pokok',String(225)),
    Column('currency',String(225)),
    Column('status',String(225)),
    Column('user_id',String(225)),
    Column('keterangan',String(225)),
    Column('selisih',String(225)),
    Column('brand',String(225)),
    Column('brutto',String(225)),
    Column('netto',String(225)),
    Column('type1',String(225)),
    Column('type2',String(225)),
    Column('pemasok',String(225)),
    Column('type3',String(225))
)