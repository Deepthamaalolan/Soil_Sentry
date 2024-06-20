import React, { useState } from 'react';
import './textarea.css';

export function Textarea({ placeholder, onMessageSend }) {
  const [message, setMessage] = useState('');

  const handleMessageChange = (event) => {
    setMessage(event.target.value);
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      onMessageSend(message);
      setMessage('');
    }
  };

  return (
    <textarea
      placeholder={placeholder}
      value={message}
      onChange={handleMessageChange}
      onKeyPress={handleKeyPress}
      className="textarea"
    />
  );
}
