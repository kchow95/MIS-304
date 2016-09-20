# Charlene Shu, Omar Olivarez, Kenneth Chow
# Program to compute compound interest
import math

# Define main function
def main():
	
	# Declare variables
	initial_amount = 1000
	num_years = 10
	min_rate = 5
	max_rate = 10
	balance = 0
	
	# Header line
	print("Year  Amount(5%)  Amount(6%)  Amount(7%)  Amount(8%)  Amount(9%) Amount(10%)")
	print("----  ----------  ----------  ----------  ----------  ---------- -----------")
	
	# Header line option 2
	'''
	print("Year  ", end='')
	for rate in range(min_rate,max_rate+1):
		print ("Amount("+str(rate)+"%)  ", end='')
	print()
	print("----  ", end='')
	for rate in range(min_rate,max_rate+1):
		print("----------  ", end='')
	print()
	'''
	
	# Table body
	for year in range(1,num_years+1):
		print("%4d" %year,end='  ')
		for rate in range(min_rate,max_rate+1):
			balance = initial_amount*math.pow((1.0+rate/100),year)
			print("{:10,.2f}" .format(balance),end='  ')
		print()

		
# Call main function
main()