# EnDec
Simple encryption and decryption CLI

Installing Libraries:
Open your terminal
Type: pip3 install -r requirements.txt

This will install all the necessary python libraries needed for the script.

Installing Git:
If you don't have Git installed then you can install it by opening your terminal and then typing
"sudo apt-get install git" without the quote marks.

Running the script:
Please use python2 to run the script.
Open your terminal and type in "python2 EnDec.py"
Make sure python2 is installed on your device if you're using Windows. Any Linux distro should have python2 installed by default.

Creating your own salt for Generate_Key_With_Pwd.py:
Open the Generate_Key_With_Pwd.py file with any text editor you want.
Open your terminal and type in python2. Right arrows should come up.
Type "import os" without the quotes. If you don't have the os module installed already, install it from the requirements.txt file.
Now type "os.urandom(any number)" without the quotes. There must be an integer argument otherwise it will not generate a salt for you. An example "os.random(32)" will generate a salt. "os.random()" return an error message.

This will generate a random salt and print it out on the terminal.
Then you copy that salt and paste it in the Generate_Key_With_Pwd.py file. Find the line that says "# salt =". Make sure there's one space after the equal sign and paste the salt. Make sure to delete the "#" hashtag which is placed before "salt =" so the script doesn't come up with an error.
