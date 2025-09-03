import bcrypt

password = 'testpassword'.encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(f"Hashed password: {hashed.decode('utf-8')}")
if bcrypt.checkpw(password, hashed):
    print("Bcrypt verification successful!")
else:
    print("Bcrypt verification failed!")