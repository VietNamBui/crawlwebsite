import { useEffect, useState } from 'react';
import { bookService } from './api';

const App = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const fetchBooks = async () => {
      const data = await bookService.getAllBooks();
      setBooks(data || []);
    };
    fetchBooks();
  }, []);

  return (
    <div>
      <h1>Danh sách Sách</h1>
      <ul>
        {books.map((book, index) => (
          <li key={index}>{book}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
