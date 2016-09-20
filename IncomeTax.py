# Charlene Shu, Omar Olivarez, Kenneth Chow
# Program that displays amount of taxes for different filing statuses

# Define main function
def main():
	
	# Declare variables
	filing_status = 0
	income = 0
	income_tax = 0
	
	# Get user input on filing status
	filing_status = eval(input("Enter filing status [(1)Single,(2)Married filing jointly,(3)Married filing separately,(4)Head of household,(-1)Quit]: "))
		if(filing_status==-1):
		income_tax = 0
	elif(not(1<=filing_status<=4)):
		print("Invalid filing status")
	else:	
		# Get user input on taxable income
		income = eval(input("Enter amount of taxable income: "))
		if(filing_status==1):
			income_tax = single_tax(income)
		if(filing_status==2):
			income_tax = married_jointly_tax(income)
		if(filing_status==3):
			income_tax = married_separately_tax(income)
		if(filing_status==4):
			income_tax = head_household_tax(income)
		# Display amount of tax
		print("The tax for the individual is ${:,.2f}" .format(income_tax))
		
# Single
def single_tax(income):
	tax = 0
	if(income>372950):
		tax = 8350*0.10+(33950-8350)*0.15+(82250-33950)*0.25+(171550-82250)*0.28+(372950-171550)*0.33+(income-372950)*0.35
	elif(income>171550):
		tax = 8350*0.10+(33950-8350)*0.15+(82250-33950)*0.25+(171550-82250)*0.28+(income-171550)*0.33
	elif(income>82250):
		tax = 8350*0.10+(33950-8350)*0.15+(82250-33950)*0.25+(income-82250)*0.28
	elif(income>33950):
		tax = 8350*0.10+(33950-8350)*0.15+(income-33950)*0.25
	elif(income>8350):
		tax = 8350*0.10+(income-8350)*0.15
	else:
		tax = income*0.10
	
	return tax
	
# Maried filing jointly
def married_jointly_tax(income):
	tax = 0
	if(income>372950):
		tax = 16700*0.10+(67900-16700)*0.15+(137050-67900)*0.25+(208850-137050)*0.28+(372950-208850)*0.33+(income-372950)*0.35
	elif(income>208850):
		tax = 16700*0.10+(67900-16700)*0.15+(137050-67900)*0.25+(208850-137050)*0.28+(income-208850)*0.33
	elif(income>137050):
		tax = 16700*0.10+(67900-16700)*0.15+(137050-67900)*0.25+(income-137050)*0.28
	elif(income>67900):
		tax = 16700*0.10+(67900-16700)*0.15+(income-67900)*0.25
	elif(income>16700):
		tax = 16700*0.10+(income-16700)*0.15
	else:
		tax = income*0.10
		
	return tax

# Married filing separately
def married_separately_tax(income):
	tax = 0
	if(income>186475):
		tax = 8350*0.10+(33950-8350)*0.15+(68525-33950)*0.25+(104425-68525)*0.28+(186475-104425)*0.33+(income-186475)*0.35
	elif(income>104425):
		tax = 8350*0.10+(33950-8350)*0.15+(68525-33950)*0.25+(104425-68525)*0.28+(income-104425)*0.33
	elif(income>68525):
		tax = 8350*0.10+(33950-8350)*0.15+(68525-33950)*0.25+(income-68525)*0.28
	elif(income>33950):
		tax = 8350*0.10+(33950-8350)*0.15+(income-33950)*0.25
	elif(income>8350):
		tax = 8350*0.10+(income-8350)*0.15
	else:
		tax = income*0.10
		
	return tax

# Head of household
def head_household_tax(income):
	tax = 0
	if(income>372950):
		tax = 11950*0.10+(45500-11950)*0.15+(117450-45500)*0.25+(190200-117450)*0.28+(372950-190200)*0.33+(income-372950)*0.35
	elif(income>190200):
		tax = 11950*0.10+(45500-11950)*0.15+(117450-45500)*0.25+(190200-117450)*0.28+(income-190200)*0.33
	elif(income>117450):
		tax = 11950*0.10+(45500-11950)*0.15+(117450-45500)*0.25+(income-117450)*0.28
	elif(income>45500):
		tax = 11950*0.10+(45500-11950)*0.15+(income-45500)*0.25
	elif(income>11950):
		tax = 11950*0.10+(income-11950)*0.15
	else:
		tax = income*0.10
		
	return tax

	
# Call main function
main()