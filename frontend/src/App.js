import React from 'react';
import './App.css';
import Chat from './Chat';
import Login from './Login';
import Register from './Register';
import logo from './logo.svg';
function App() {
  return (
    <div className="App">
      
      <Register />
      <Login />
      <Chat />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
