#Submission from Kenneth Chow, Omar Olivarez, and Charlene Shu.

# Program that receives sales person ID and the units sold by the sales person


# Displays maximum units sold and the sales person number who sold those maximum units

import tkinter.messagebox

# Define main function
def main():
	# Declare variables
	units_sold1 = 0
	units_sold2 = 0
	units_sold3 = 0
	units_sold4 = 0
	units_sold5 = 0
	sales_ID1 = 0
	sales_ID2 = 0
	sales_ID3 = 0
	sales_ID4 = 0
	sales_ID5 = 0
	max_units = 0
	max_ID = 0
	message = ""
	
	# Get user input
	sales_ID1, units_sold1 = eval(input("Enter sales person ID and units sold (both integers): "))
	sales_ID2, units_sold2 = eval(input("Enter sales person ID and units sold (both integers): "))
	sales_ID3, units_sold3 = eval(input("Enter sales person ID and units sold (both integers): "))
	sales_ID4, units_sold4 = eval(input("Enter sales person ID and units sold (both integers): "))
	sales_ID5, units_sold5 = eval(input("Enter sales person ID and units sold (both integers): "))
	
	#Assume units_sold1 is maximum
	max_units = units_sold1
	max_ID = sales_ID1
	if(units_sold2 > max_units):
		max_units = units_sold2
		max_ID = sales_ID2
	if(units_sold3 > max_units):
		max_units = units_sold3
		max_ID = sales_ID3
	if(units_sold4 > max_units):
		max_units = units_sold4
		max_ID = sales_ID4
	if(units_sold5 > max_units):
		max_units = units_sold5
		max_ID = sales_ID5
	
	# Set message
	message = "Maximum units sold: %d\nWinning sales person: %d" %(max_units, max_ID)
	tkinter.messagebox.showinfo("Maximum Sales", message)
		

# Run the main function
main()
