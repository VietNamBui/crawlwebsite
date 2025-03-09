# Project Overview
![image](https://github.com/user-attachments/assets/cc7ef15f-c968-4b4f-b065-a2d753c7a368)

This project is designed to collect, process, and display web data using Scrapy. The system is containerized with Docker for easy deployment and scalability.

## Technology
- **Docker**: Manages deployment and ensures portability.
- **JavaScript, HTML, Python**: Core development languages.
- **Redis**: Acts as a caching layer to optimize performance.
- **Scrapy**: Used for web scraping.
- **MongoDB**: Stores scraped data for long-term persistence.
- **Docker**: Packaging and Deployment.

## How to Use This Project
1. Install Docker Desktop.
2. Clone this repository to your local machine.
3. Run the `docker-compose` file.
4. Access the project at `localhost:8080`.  
   *(Ensure to stop any processes currently using this port beforehand to avoid conflicts.)*

## Backend Components
- **Scrapy**: Targets the Omega+ website to extract relevant data.
- **Redis**: Temporarily caches scraped data before moving it to MongoDB.
- **MongoDB**: Structured data storage for long-term retrieval.
- **API**: Facilitates communication between the backend and frontend.

## Frontend Components
- **Web UI**: Displays crawled data in an interactive interface.
- **Docker**: Ensures seamless deployment and scalability.

## Backend Details

### Scrapy
The scraping process specifically targets the Omega+ website, extracting and collecting relevant data.

### Redis
Data scraped by Scrapy is initially stored in Redis for caching purposes to enhance system performance.

### MongoDB
Scraped data is then transferred from Redis and stored in MongoDB for long-term persistence. This structured data can be efficiently retrieved for additional processing.

![image](https://github.com/user-attachments/assets/15cab9bd-8194-48e0-a038-3c12b6b41da9)

### API
The backend API provides access to the collected data in a structured format upon request.

![image](https://github.com/user-attachments/assets/af464551-3016-46db-96e7-9e56c92183aa)

## Frontend
When accessing `localhost:8080` in a web browser, the frontend presents the crawled data in an interactive, user-friendly interface.

![image](https://github.com/user-attachments/assets/f942d6eb-8c41-443a-bce2-0681553460a6)

---

This setup ensures an efficient, scalable, and maintainable web scraping and data visualization system.
