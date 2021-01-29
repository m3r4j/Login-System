import os # Checking if files exist or not
import sys # Used to exit
import getpass # Hide password input whle being typed
from colorama import Fore, Back, Style # Colors
from hashlib import sha256 # Used to hash the passwords
from sys import platform # Check which platform someone is on to clear the screen everytime the program is run

# Filename that is always being readed and writed to
fileName = 'REC.DAT'


# A function to get the files contents
def getFile(filename):
	with open(filename, 'r') as file:
		result = file.readlines()

		# Get rid of \n characters
		for lines in range(len(result)):
			result[lines] = result[lines].rstrip('\n')


	return result


# Check if a username is taken or already used by someone else
def usernameTaken(username):
	# Get the contents
	contents = getFile(fileName)


	# Go through the contents and see if their is any matches
	if username in contents:
		return True

	return False



# Clear the screen depending on what platform you are on, the command will be different, e.g: cls (windows), clear (linux)
def clearScreen():
	# Linux
	if platform == "linux" or platform == "linux2":
		os.system('clear')

	# OS X
	elif platform == "darwin":
		os.system('clear')

	# Windows
	elif platform == "win32":
		os.system('cls')



# Create the file needed to run the program
def createFile():
	with open(fileName, 'a'): pass


# Register function, asks for username and password. The password will be hashed with the sha256 algorithm
def register():
	# Ask for username
	username = input(Fore.CYAN + 'Username: ')

	# if username is taken
	if usernameTaken(username):
		# Show an error message in red and wait for user to respond with input
		print(Fore.RED + 'Username has already been taken.')
		input()
		return

	# Ask for password
	password = getpass.getpass('Password: ')

	# Hashes it
	password = sha256(password.encode('utf-8')).hexdigest()

	# Writes the result to the main file
	result = f'\n\n{username}\n{password}'

	with open(fileName, 'a') as file:
		file.write(result)

	print(Fore.WHITE + f'"{username}" has been added to {fileName}')
	input()



# Login function which asks for username and password
def login():
	# Get the file's contents before prompting user
	contents = getFile(fileName)

	# Username and password
	username = input(Fore.YELLOW + 'Username: ')

	# Check if username exists
	if username not in contents:
		print(Fore.RED + f'"{username}" was not found in {fileName}')
		input()
		return
		
	# Gets the index of the hash in database and compares it with password hash
	index = contents.index(username) + 1

	# Prompt user
	password = getpass.getpass('Password: ')

	# Hashes it
	password = sha256(password.encode('utf-8')).hexdigest()

	# Compares it 
	if password == contents[index]:
		print(Fore.MAGENTA + f'You have successfully signed into {username}')
	else:
		print(Fore.RED + f'Username or password was not found in {fileName}')

	input()
	return





# Main function to run everything
def main():
	# Main loop
	while True:
		clearScreen()

		# Check if REC.DAT does not exist
		if not os.path.exists('REC.DAT'):
			createFile()

		# Display prompt
		print(Fore.BLUE + '''
1. Login
2. Register
3. Exit
		''')

		# Ask user for an option and clear the screen for next output from different function
		option = input(Fore.GREEN + 'Enter your option: ')
		clearScreen()

		# Check options
		if option == '1':
			login()

		elif option == '2':
			register()

		else:
			sys.exit()

# Running
main()