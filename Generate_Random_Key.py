from cryptography.fernet import Fernet
import os
import time

key = Fernet.generate_key()
time.sleep(1)
print(key)

file = open("key.key", "wb")
file.write(key)
file.close()
os.path.abspath("key.key")

time.sleep(1)
print("\nKey has been created and saved to " + os.path.abspath("key.key") + "." + "Do not rename the key. Also remember to keep the key in a safe place...
      
