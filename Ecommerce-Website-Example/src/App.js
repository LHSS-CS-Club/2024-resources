import React, { useState } from 'react';
import MyForm from './MyForm';
import Items from './Items';
import './style.css';

export default function App() {
  const [items, setItems] = useState([]);
  return (
    <div>
      <h1>Hello CS Club!</h1>
      <p>Today, we are creating a form using React!</p>
      <MyForm items={items} setItems={setItems} />
      <Items items={items} />
    </div>
  );
}
