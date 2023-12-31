import axios from 'axios';
import React, { useState } from 'react';

function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/register', {
        username,
        email,
        password,
      });
      console.log('Registered:', response.data);
    } catch (error) {
      console.error('Registration failed:', error);
    }
  }

  return (
    <div>
      <h2>Register</h2>
      <input 
        type="text"
        placeholder="Username" 
        value={username} 
        onChange={e => setUsername(e.target.value)} />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input 
        type="password" 
        placeholder="Password" 
        value={password} 
        onChange={e => setPassword(e.target.value)} />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;
