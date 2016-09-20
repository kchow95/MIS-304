# Charlene Shu, Omar Olivarez, Kenneth Chow
#Checks if the password given is valid
def main():
	
	password = input("Please type a valid password: ")
	checkPassword(password)
	#Checks if the password has at least 8 characters
def checkPassword(password):
	good_pass = True
	special_char = ['!','@','#','$','%','^','&','*','(',')']
	if len(password) < 8:
		print("Must have a length of 8 or greater")
		good_pass = False

	#uses the ascii values to check if it has an upper or lower case
	elif password.lower() <= password or password.upper() >= password:
		print("Must be have an upper and a lower case letter")
		good_pass = False
	else:
		num_count = 0
		#Checks if the password has at least 2 numbers
		for char in password:
			for num in range(9):
				if char == str(num):
					num_count +=1
		if num_count < 2:
			print("Must have at least 2 numbers")
			good_pass = False
		else:
			has_char = False
			for char2 in password:
				for char3 in special_char:
					if char2 == char3:
						has_char = True
			if(has_char == False):
				print("Must have a special character")
			good_pass = has_char

	if(good_pass):
		print("The password you entered is valid")
	else: 
		print('The password you entered is invalid')


main()