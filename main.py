from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Produk(BaseModel):
    id: str
    name: str
    category: str
    location:str
    price:int
    condition:str
    publish_date:str

# Data dummy Produk
produk_data = {
    "data":
    [
        {"id": "1", "name": "Rexus Daxa Asteria V2", "type": "Controller","location":"Bandung", "price":300000, "condition":"Very Good Condition", "publish_date":"2024-05-08"},
    ],
    "message":"success", "error":"false"
}

@app.get("/daftar_produk")
async def get_produk():
    return produk_data


@app.get("/detail_produk/{produk_id}", response_model=Produk)
async def get_produk_detail(produk_id: str):
    for produk in produk_data["data"]:
        if produk["id"] == produk_id:
            return produk
    return {"message": "Produk not found"}