# Sử dụng Python image nhẹ
FROM python:3.9-slim

# Đặt thư mục làm việc bên trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt .

# Cài đặt thư viện Python
RUN apt-get update && apt-get install -y libpq-dev libmariadb-dev-compat libmariadb-dev pkg-config python3-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn dự án vào container
COPY . .

# Chạy lệnh Scrapy
CMD ["scrapy", "crawl", "nambui_omega_spider"]



