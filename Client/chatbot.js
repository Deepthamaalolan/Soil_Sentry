import React, { useState, useEffect } from 'react';
import { Button } from './button';
import { Textarea } from './textarea';
import './chatbot.css';

export function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [options, setOptions] = useState(['Soil Analysis', 'Weather Update', 'Crop Recommendation']);

  useEffect(() => {
    const initialMessage = {
      text: 'Hi, I am Hydrabot. How can I help you?',
      fromUser: false,
      options: options
    };
    setMessages([initialMessage]);
  }, []);

  const handleMessageSend = async (message) => {
    if (message.trim()) {
      const newMessage = { text: message, fromUser: true };
      setMessages([...messages, newMessage]);

      // Placeholder for API call
      try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ user_input: message })
        });
        const data = await response.json();
        const botResponse = { text: data.message, fromUser: false };
        setMessages((prevMessages) => [...prevMessages, botResponse]);
      } catch (error) {
        console.error('Error calling the API', error);
      }
    }
  };

  const handleOptionClick = (option) => {
    handleMessageSend(option);
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <h2>Soil Sentry</h2>
      </div>
      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.fromUser ? 'user' : 'bot'}`}>
            {message.text}
            {!message.fromUser && message.options && (
              <div className="options">
                {message.options.map((option, i) => (
                  <button key={i} className="option-button" onClick={() => handleOptionClick(option)}>
                    {option}
                  </button>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
      <div className="input-container">
        <Textarea placeholder="Type your message here." onMessageSend={handleMessageSend} />
        <Button onClick={() => handleMessageSend(document.querySelector('.textarea').value)}>Send</Button>
      </div>
    </div>
  );
}
