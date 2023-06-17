from fastapi import APIRouter
from config.db import conn
from models.barang import barangs
from schemas.barang import Barang

barang = APIRouter()

@barang.get("/")
async def read_data():
    return conn.execute(barangs.select()).fetchall()

@barang.get("/{jenis}")
async def read_data(jenis: str):
    return conn.execute(barangs.select().where(barangs.c.jenis == jenis)).fetchall()

@barang.post("/")
async def write_data(barang: Barang):
    conn.execute(barangs.insert().values(
        jenis=barang.jenis,
        kategori=barang. kategori,
        kode_barang=barang.kode_barang,
        nama_barang=barang.nama_barang,
        style=barang.style,
        color=barang.color,
        size=barang.size,
        hs_code=barang.hs_code,
        im=barang.im,
        satuan=barang.satuan,
        harga=barang.harga,
        harga_pokok=barang.harga_pokok,
        password=barang.password,
        currency=barang.currency,
        status=barang.status,
        user_id=barang.user_id,
        keterangan=barang.keterangan,
        selisih=barang.selisih,
        brand=barang.brand,
        brutto=barang.brutto,
        netto=barang.netto,
        type1=barang.type1,
        type2=barang.type2,
        pemasok=barang.pemasok,
        type3=barang.type3
    ))
    return conn.execute(barangs.select()).fetchall()

@barang.put("/{id}")
async def update_data(id:int,barang: Barang):
    conn.execute(barangs.update(
        jenis=barang.jenis,
        kategori=barang. kategori,
        kode_barang=barang.kode_barang,
        nama_barang=barang.nama_barang,
        style=barang.style,
        color=barang.color,
        size=barang.size,
        hs_code=barang.hs_code,
        im=barang.im,
        satuan=barang.satuan,
        harga=barang.harga,
        harga_pokok=barang.harga_pokok,
        password=barang.password,
        currency=barang.currency,
        status=barang.status,
        user_id=barang.user_id,
        keterangan=barang.keterangan,
        selisih=barang.selisih,
        brand=barang.brand,
        brutto=barang.brutto,
        netto=barang.netto,
        type1=barang.type1,
        type2=barang.type2,
        pemasok=barang.pemasok,
        type3=barang.type3
    ).where(barangs.c.id == id))
    return conn.execute(barangs.select()).fetchall()

@barang.delete("/")
async def delete_data():
    conn.execute(user.delete().where(barangs.c.id == id))
    return conn.execute(barangs.select()).fetchall()