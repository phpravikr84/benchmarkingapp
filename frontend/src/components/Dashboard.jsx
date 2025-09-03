import React, { useState, useEffect } from 'react';
import { authAPI } from '../services/api';

const Dashboard = ({ user, onLogout }) => {
  const [dashboardData, setDashboardData] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const response = await authAPI.dashboard();
      setDashboardData(response.data.message);
    } catch (error) {
      setError(error.response?.data?.error || 'Failed to fetch dashboard data');
      if (error.response?.status === 401) {
        onLogout();
      }
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="text-center">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="card shadow">
            <div className="card-body p-4">
              <h2 className="card-title text-center mb-4">Dashboard</h2>
              
              {error && (
                <div className="alert alert-danger" role="alert">
                  {error}
                </div>
              )}

              <div className="text-center mb-4">
                <h4 className="text-success">{dashboardData}</h4>
              </div>

              <div className="card mb-4">
                <div className="card-header">
                  <h5 className="card-title mb-0">User Information</h5>
                </div>
                <div className="card-body">
                  <div className="row">
                    <div className="col-md-6">
                      <p><strong>Username:</strong> {user.username}</p>
                      <p><strong>Email:</strong> {user.email}</p>
                    </div>
                    <div className="col-md-6">
                      <p><strong>First Name:</strong> {user.firstname}</p>
                      <p><strong>Last Name:</strong> {user.lastname}</p>
                    </div>
                  </div>
                  <p className="mb-0"><strong>Status:</strong> 
                    <span className="badge bg-success ms-2">{user.status}</span>
                  </p>
                </div>
              </div>

              <div className="text-center">
                <button onClick={onLogout} className="btn btn-danger">
                  Logout
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;