Project Overview
This project is designed to collect, process, and display web data using Scrapy. The system is containerized with Docker for easy deployment and scalability.
Technology
Tech: Docker, JS, HTML, Python, Redis, Scrapy, MongoDB
Backend Components
•	Scrapy: Used for web scraping.
•	MongoDB: Stores the scraped data for long-term persistence.
•	Redis: Acts as a caching layer to optimize performance.
•	API: Facilitates communication between the backend and frontend.
Frontend Components
•	Web UI: Displays the crawled data in an interactive interface.
•	Docker: Manages the deployment and ensures portability.
Backend Details
Scrapy
The scraping process targets the Omega+ website, extracting relevant data.
Redis
Scraped data is initially stored in Redis for caching before being moved to MongoDB for long-term storage.
MongoDB
MongoDB stores the structured data, making it easily retrievable for further processing. The data is saved as follows:
 
API
The backend API serves the collected data in a structured format upon request. The data is saved as follows:
 
Frontend
When accessing localhost:8080 in a web browser, the frontend presents the crawled data in a user-friendly interface.
 
This setup ensures an efficient, scalable, and maintainable web scraping and data visualization system.

