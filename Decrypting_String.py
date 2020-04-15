from cryptography.fernet import Fernet

file = open("key.key", "rb")
key = file.read()
file.close()

message = raw_input("Enter the encrypted text.: ")
encrypted = message

f = Fernet(key)
decrypted_string = f.decrypt(encrypted)

original_message = decrypted_string.decode()
print(original_message)
