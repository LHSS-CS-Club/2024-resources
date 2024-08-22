import React from 'react';

const itemList = [
  { name: 'Item1', description: 'This is a description' },
  { name: 'Item2', description: 'This is a description' },
  { name: 'Item3', description: 'This is a description' },
  { name: 'Item4', description: 'This is a description' },
  { name: 'Item5', description: 'This is a description' },
];

function Items({ items }) {
  return (
    <div>
      <h1>Items</h1>
      <div className="itemsContainer">
        {items.map((v, i) => {
          return (
            <div key={i} index={i} className="item">
              <div className="name">{v.name}</div>
              <div className="price">${v.price}</div>
              <div className="description">{v.description}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default Items;
