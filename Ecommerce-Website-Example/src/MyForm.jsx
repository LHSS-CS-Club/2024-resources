import React, { useState } from 'react';

function MyForm({ items, setItems }) {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');

  const handleNameChange = (e) => {
    console.log(e.target.value);
    setName(e.target.value);
  };

  const handlePriceChange = (e) => {
    console.log(e.target.value);
    setPrice(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    console.log(e.target.value);
    setDescription(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form data submitted:', name, description);
    const newItems = [
      ...items,
      { name: name, description: description, price: price },
    ];
    setItems(newItems);
    setName('');
    setDescription('');
    setPrice('');
  };

  return (
    <div>
      <div>
        <h2>Get Customer Data Survey</h2>
        <form onSubmit={handleSubmit} className="form">
          <div className="input">
            <label htmlFor="username">Name:</label>
            <input
              type="text"
              id="name"
              name="name"
              value={name}
              onChange={handleNameChange}
            />
          </div>
          <div className="input">
            <label htmlFor="username">Price:</label>
            <input
              type="text"
              id="price"
              name="price"
              value={price}
              onChange={handlePriceChange}
            />
          </div>
          <div className="input">
            <label htmlFor="password">Description:</label>
            <input
              type="text"
              id="description"
              name="description"
              value={description}
              onChange={handleDescriptionChange}
            />
          </div>
          <div>
            <button className="submitButton" type="submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default MyForm;
