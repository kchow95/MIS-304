#Submission from Kenneth Chow, Omar Olivarez, and Charlene Shu.


#Program to read integer and print odd/even

import tkinter.messagebox

#declare the main function
def main():
	#Declare variables 
	number = 0
	message = ""
	isOdd = False
	
	#Get user input "Enter an integer:", leaving cursor on same line
	number = int(input("Enter an integer: "))
	
	#isOdd if remainder after dividing by 2 is 1
	isOdd = (number % 2 == 1)
	
	#Set the message
	if(isOdd):
		message = "Number " + str(number) + " is an Odd number"
	else:
		message = "Number " + str(number) + " is an Even number"
	
	#Display message
	tkinter.messagebox.showinfo("Even or Odd",message)

#Call the main function
main()
