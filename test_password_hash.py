from werkzeug.security import check_password_hash, generate_password_hash

# Test the current hash
stored_hash = "scrypt:32768:8:1$h2D3x68qFhGlEMO3$87a39f7fb5370aa9d6e9fb2e4f342ac53f69e63efc095e41eea052b1ff8cfbf03971acb143194ad02f2cd9"
password = "123456789"

print(f"Stored hash: {stored_hash}")
print(f"Password to check: {password}")
print(f"Check result: {check_password_hash(stored_hash, password)}")

# Generate a new hash with the same password to compare
new_hash = generate_password_hash(password)
print(f"New generated hash: {new_hash}")
print(f"New hash check: {check_password_hash(new_hash, password)}")