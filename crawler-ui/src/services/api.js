import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' }
});

export const bookService = {
  getAllBooks: async () => {
    try {
      const response = await api.get('/data');
      return response.data["scrapy:book_urls"];
    } catch (error) {
      console.error("API Error:", error);
      return [];
    }
  }
};
