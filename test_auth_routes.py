import requests

base_url = 'http://localhost:80/auth'

# Test registration
register_data = {
    'username': 'testuser2',
    'password': 'testpassword2',
    'firstname': 'Jane',
    'lastname': 'Smith',
    'email': 'jane.smith@example.com'
}
response = requests.post(f'{base_url}/register', json=register_data)
print('Register:', response.json())


# Test login with username
'''
login_data = {
    'identifier': 'testuser2',
    'password': 'testpassword2'
}
response = requests.post(f'{base_url}/login', json=login_data)
print('Login (username):', response.json(), response.status_code)
access_token = response.json().get('access_token')

# Test login with email
login_data = {
    'identifier': 'jane.smith@example.com',
    'password': 'testpassword2'
}
response = requests.post(f'{base_url}/login', json=login_data)
print('Login (email):', response.json(), response.status_code)

# Test dashboard (protected route)
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(f'{base_url}/dashboard', headers=headers)
print('Dashboard:', response.json(), response.status_code)
'''