import React, { useState } from 'react';

function MyForm() {
  const [name, setName] = useState('');
  const [feedback, setFeedback] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleNameChange = (e) => {
    console.log(e.target.value);
    setName(e.target.value);
  };

  const handleFeedbackChange = (e) => {
    console.log(e.target.value);
    setFeedback(e.target.value);
  };

  const handleSubmit = () => {
    console.log('Form data submitted:', name, feedback);
    setIsSubmitted(true);
  };

  return (
    <div>
      {isSubmitted ? (
        <div>
          <div>Thanks for the feedback</div>
          <div>Name: {name}</div>
          <div>Feedback: {feedback}</div>
        </div>
      ) : (
        <div>
          <h2>Get Customer Data Survey</h2>
          <form onSubmit={handleSubmit}>
            <div>
              <label htmlFor="username">Name:</label>
              <input
                type="text"
                id="name"
                name="name"
                value={name}
                onChange={handleNameChange}
              />
            </div>
            <div>
              <label htmlFor="password">Feedback/Comments:</label>
              <input
                type="text"
                id="feedback"
                name="feedback"
                value={feedback}
                onChange={handleFeedbackChange}
              />
            </div>
            <div>
              <button type="submit">Submit</button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
}

export default MyForm;
