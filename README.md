# EnDec
Simple encryption and decrytion CLI

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
Open your terminal and type in python2. Right arrows shoud come up.
Now type "os.urandom()" without the quotes. This will generate a random salt and print it out on the terminal.
Then you copy that salt and paste it on the line that says "salt =". Make sure to delete the "#" hashtag before "salt =" so the script will be able to run.
