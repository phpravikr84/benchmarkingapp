import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/auth';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authAPI = {
  login: (identifier, password) => 
    api.post('/login', { identifier, password }),

  register: (userData) => 
    api.post('/register', userData),

  dashboard: () => 
    api.get('/dashboard'),
};

export default api;