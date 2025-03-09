from fastapi import FastAPI
import json
import redis
from config import redis_client, mongo_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các nguồn gốc (cẩn thận khi sử dụng trong production)
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả phương thức HTTP
    allow_headers=["*"],  # Cho phép tất cả các headers
)
r = redis.Redis(host="redis_db", port=6379, db=0)

@app.get("/data")
async def get_all_data():
    key = "scrapy:book_urls"
    key_type = r.type(key).decode()

    if key_type == "string":
        data = r.get(key).decode()
    elif key_type == "list":
        data = r.lrange(key, 0, -1)  # Lấy tất cả phần tử trong list
        data = [item.decode() for item in data]  # Giải mã từ bytes
    elif key_type == "set":
        data = list(r.smembers(key))  # Lấy tất cả phần tử trong set
        data = [item.decode() for item in data]
    else:
        data = {"error": f"Unsupported data type: {key_type}"}

    return {"scrapy:book_urls": data}
