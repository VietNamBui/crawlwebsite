from pymongo import MongoClient
import redis
import os

# Lấy thông tin từ biến môi trường (Docker)
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")

# Kết nối Redis
redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

# Kết nối MongoDB
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["BookstoreDB"]  # Thay tên DB thực tế
