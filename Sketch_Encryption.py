import os
import time
import subprocess

try:
	print ("[+]Thank you for using my program. To report bugs, please email quinb96@protonmail.com[+]")
	time.sleep(5)

	subprocess.call(["clear"])

	print ("""

		[1] Generate a key with password
		[2] Generate a random key
		[3] Encrypt text
		[4] Encrypt a file
		[5] Decrypt text
		[6] Decrypt a file

		""")
	Choice = raw_input("Select what you want to do. ")

	if Choice == "1":
		subprocess.call(["clear"])
		import Generate_Key_With_Pwd.py
	elif Choice == "2":
		subprocess.call(["clear"])
		import Generate_Random_Key.py
	elif Choice == "3":
		subprocess.call(["clear"])
		import Encrypting_String.py
	elif Choice == "4":
		subprocess.call(["clear"])
		import Encrypting_File.py
	elif Choice == "5":
		subprocess.call(["clear"])
		import Decrypting_String.py
	elif Choice == "6":
		subprocess.call(["clear"])
		import Decrypting_File.py
except:
	KeyboardInterrupt()
	time.sleep(1)
	
	print "\n\nWould you like to go back to the main menu?"
	time.sleep(2)
	Choice = raw_input("y/n?: ")

	if Choice == "y":
		subprocess.call(["python2", "Sketch_Encryption.py"])
	elif Choice == "n":
		time.sleep(1)
		print"\nExiting script...Go to github page to report issues."
		time.sleep(3)
		quit()