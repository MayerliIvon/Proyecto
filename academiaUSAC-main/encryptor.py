from cryptography.fernet import Fernet

# Generate a key for Fernet and save it to a file
key = Fernet.generate_key()
with open('key.txt', 'wb') as file:  # 'wb' as the key is in bytes
    file.write(key)

# Encrypt a message
def Encrypt(message):
    with open('key.txt', 'rb') as file:  # 'rb' to read bytes
        key = file.read()
    
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt an encrypted message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message
