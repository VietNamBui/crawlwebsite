# Sử dụng Python image
FROM python:3.10

# Đặt thư mục làm việc
WORKDIR /app

# Copy files vào container
COPY route.py config.py /app/

# Cài đặt FastAPI và các thư viện cần thiết
RUN pip install fastapi[all] pymongo redis uvicorn

# Chạy API khi container khởi động
CMD ["uvicorn", "route:app", "--host", "0.0.0.0", "--port", "8000"]
