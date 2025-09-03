import React from 'react';

const Navbar = ({ user, onLogout }) => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container">
        <span className="navbar-brand">Benchmarking App</span>
        
        {user && (
          <div className="navbar-nav ms-auto">
            <span className="nav-item nav-link text-white">
              Welcome, {user.username}
            </span>
            <button className="btn btn-outline-light btn-sm ms-2" onClick={onLogout}>
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;