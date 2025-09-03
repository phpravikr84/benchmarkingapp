import React, { useState } from 'react';
import { authAPI } from '../services/api';
import backgroundImage from '../../assets/images/login-reg-bg.jpg';

const Login = ({ onLogin, switchToRegister }) => {
  const [formData, setFormData] = useState({
    identifier: '',
    password: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await authAPI.login(formData.identifier, formData.password);
      const { access_token, user } = response.data;
      
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('user', JSON.stringify(user));
      onLogin(user);
    } catch (error) {
      setError(error.response?.data?.error || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      <div className="login-left">
        <div className="login-content">
          <div className="app-brand">Benchmarking App</div>
          
          <div className="welcome-text">
            <h2>Welcome to Benchmarking App <br/>
            Sign in to your account.</h2>
          </div>
          
          {error && (
            <div className="alert alert-danger" role="alert">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit}>
            <input
              type="text"
              className="form-control"
              name="identifier"
              value={formData.identifier}
              onChange={handleChange}
              placeholder="Username or Email"
              required
            />
            
            <input
              type="password"
              className="form-control"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Password"
              required
            />

            <button 
              type="submit" 
              className="btn-login"
              disabled={loading}
            >
              {loading ? 'Logging in...' : 'Login'}
            </button>
          </form>

          <div className="auth-footer">
            Don't have an account?{' '}
            <button 
              type="button" 
              onClick={switchToRegister} 
              className="btn-link"
            >
              Signup here
            </button>
          </div>
        </div>
      </div>
      
      <div className="login-right" style={{ backgroundImage: `url(${backgroundImage})` }}>
        {/* Background image will be displayed here */}
      </div>
    </div>
  );
};

export default Login;