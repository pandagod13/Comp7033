import secrets
secret_key = secrets.token_hex(16)  # Generates a secure 32-character hex token
print(secret_key)
