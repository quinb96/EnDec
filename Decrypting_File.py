from cryptography.fernet import Fernet
import os
import time

file = open("key.key", "rb")
key = file.read()
file.close()

Text_File = raw_input("Enter the path of the text file you want to decrypt.: ")
os.path.abspath(Text_File)

with open(os.path.abspath(Text_File), "rb") as f:
	data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)

Text_File = Text_File.replace(".enc", "")
with open(Text_File, "wb") as f:
	f.write(decrypted)
