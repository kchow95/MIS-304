# Charlene Shu, Omar Olivarez, Kenneth Chow
#Program to check card validation
#Define main function
def main():
	input_user = input("Please input a valid credit card number: ")
	#Checks if the card is valid and prints accordingly
	if isValid(input_user):
		print(getTypeCard(input_user[0]))
		print("The number is valid")
	else:
		print("Your credit card number is invalid")
#define isvalid returns true if the card is valid
def isValid(card_number):
	valid_card = True
	#Checks the numbers first
	check_numbers = (sumOfDoubleEvenPlace(card_number) + sumOfOddPlace(card_number))%10

	prefix = getPrefix(card_number)
	#checks the parameters for the card
	#not long enough or too long
	if 13 >= getSize(card_number) >=16:
		valid_card = False
	#the numbers don't add up
	elif(check_numbers != 0):
		valid_card = False
	#prefix isn't valid
	elif prefixMatched(card_number, prefix) == False:
		print(prefix)
		valid_card = False

	return valid_card 
#sums the even places with double the int		
def sumOfDoubleEvenPlace(card_number):
	
	step = len(card_number)-2
	total = 0
	while step >= 0:
		total+= (getDigit(2*int(card_number[step])))
		step-=2
	return total

#Gets the digit for the double even place function, takes out the 10s place and subtracts by one
def getDigit(digit):

	return_digit = digit
	if(digit >= 10):
		return_digit = (digit - 10) + 1
	return return_digit

#Gets the digit for the odd places from the end of the card_number and sums them
def sumOfOddPlace(card_number):
	step = len(card_number)-1
	total = 0
	while step >= 0:
		total += int(card_number[step])
		step -= 2
	return total
#Checks the number d if it falls into one of the four categories
def prefixMatched(card_number, d):

	if(int(d) != 4 and int(d) != 5 and int(d) != 6 and int(d) != 37):
		return False
	else: 
		return True
#returns the size of the card number
def getSize(card_number): 
	return len(card_number)


#Returns the type of card it is
def getTypeCard(num):

	num = int(num)
	if(num == 4):
		return "Your card type is Visa"
	elif(num == 5): 
		return "Your card type is MasterCard"
	elif(num == 6):
		return "Your card type is Discover"
	else:
		return "Your card type is American Express"

#gets the second number if the card starts with a 3
def getPrefix(card_number):
	if card_number[0] == "3":
		return card_number[:2]
	else:
		return card_number[0]
main()



