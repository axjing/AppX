import axios from 'axios';
import React, { useState } from 'react';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/login', {
        username,
        password,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      console.log('Logged in:', response.data);
    } catch (error) {
      console.error('Login failed:', error.response.data.detail);
    }
  }

  return (
    <div>
      <h2>Login</h2>
      <input
        type="text"
        placeholder="Username" 
        value={username} 
        onChange={e => setUsername(e.target.value)} />
      <input 
        type="password" 
        placeholder="Password" 
        value={password} 
        onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;
