from fastapi import FastAPI
# from routes.index import user
from routes.indexBarang import barang 
app = FastAPI()

app.include_router(barang)