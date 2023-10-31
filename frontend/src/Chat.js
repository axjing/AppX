import React, { useState } from 'react';
import axios from 'axios';

function Chat() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit = async () => {
    if (input) {
      // 向FastAPI后端发送POST请求
      try {
        const response = await axios.post('http://localhost:8000/chat', { prompt: input });
        const reply = response.data.response;

        // 更新消息列表
        setMessages([...messages, { text: input, isUser: true }, { text: reply, isUser: false }]);
        setInput('');
      } catch (error) {
        console.error('Chat request failed:', error);
      }
    }
  };

  return (
    <div>
      <div className="chat-box">
        {messages.map((message, index) => (
          <div key={index} className={message.isUser ? 'user' : 'bot'}>
            {message.text}
          </div>
        ))}
      </div>
      <div className="input-box">
        <input
          type="text"
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button onClick={handleSubmit}>Send</button>
      </div>
    </div>
  );
}

export default Chat;