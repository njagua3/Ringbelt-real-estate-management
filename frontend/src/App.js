// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Tenants from './components/Tenants';
import Landlords from './components/Landlords';
import Properties from './components/Properties';
import './App.css';  // Import CSS for styling

const App = () => {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>Tenant Management System</h1>
          <nav>
            <ul>
              <li><Link to="/">Home</Link></li>
              <li><Link to="/tenants">Tenants</Link></li>
              <li><Link to="/landlords">Landlords</Link></li>
              <li><Link to="/properties">Properties</Link></li>
            </ul>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/tenants" element={<Tenants />} />
            <Route path="/landlords" element={<Landlords />} />
            <Route path="/properties" element={<Properties />} />
            <Route path="/" element={<h2>Welcome to the Tenant Management System!</h2>} />
          </Routes>
        </main>
        <footer>
          <p>&copy; 2024 Ringbelt Real Estate Agency</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
