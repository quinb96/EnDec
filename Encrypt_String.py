from cryptography.fernet import Fernet
import time

file = open("key.key", "rb")
key = file.read()
file.close()

message = raw_input("Enter msg you want to encrypt: ")
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
print("Encrypted: " + encrypted)
file.write(encrypted)
