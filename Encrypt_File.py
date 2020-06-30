from cryptography.fernet import Fernet
import os

EncText = raw_input("Select file you want to encrypt: ")
os.path.abspath(EncText)

file = open("key.key", "rb")
key = file.read()
file.close()

with open(EncText, "rb") as f:
	data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

filename = raw_input("What do you wanna name the file?: (Add .txt to the end of the filename): ")

with open(filename + ".enc", "wb") as f:
	f.write(encrypted)
	print "File has been encrypted and saved as " + filename + ".enc" + "\n"
