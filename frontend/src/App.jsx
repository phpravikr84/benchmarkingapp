import React, { useState, useEffect } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import Navbar from './components/Navbar';

function App() {
  const [currentView, setCurrentView] = useState('login');
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    const userData = localStorage.getItem('user');
    
    if (token && userData) {
      setUser(JSON.parse(userData));
      setCurrentView('dashboard');
    }
  }, []);

  const handleLogin = (userData) => {
    setUser(userData);
    setCurrentView('dashboard');
  };

  const handleRegister = (userData) => {
    setUser(userData);
    setCurrentView('dashboard');
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    setUser(null);
    setCurrentView('login');
  };

  const switchToRegister = () => setCurrentView('register');
  const switchToLogin = () => setCurrentView('login');

  return (
    <div className="App">
      {/* <Navbar user={user} onLogout={handleLogout} /> */}
      
      <main>
        {currentView === 'login' && (
          <Login onLogin={handleLogin} switchToRegister={switchToRegister} />
        )}
        
        {currentView === 'register' && (
          <Register onRegister={handleRegister} switchToLogin={switchToLogin} />
        )}
        
        {currentView === 'dashboard' && user && (
          <Dashboard user={user} onLogout={handleLogout} />
        )}
      </main>
    </div>
  );
}

export default App;