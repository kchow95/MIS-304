# Charlene Shu, Omar Olivarez, Kenneth Chow
# Program that displays total value of products sold

# Define main function
def main():
	
	# Declare variables
	product_id = 0
	quantity_sold = 0
	total_price = 0
	total_sold = 0
	
	# Get user input for product ID
	product_id = eval(input("Enter product ID, (-1 to finish): "))
	while(product_id != -1):
		if(1<=product_id<=5):
			# Get user input for quantity sold
			# Update total price and total quantity sold 
			quantity_sold = eval(input("Enter quantity sold: "))
			total_price += retail_price(product_id)*quantity_sold
			total_sold += quantity_sold
		else:
			print("Product ID is incorrect.")
		product_id = eval(input("Enter another product ID, (-1 to finish): "))
	
	# Print value of total products sold
	if(total_sold<=0):
		print("No items sold")
	else:
		print("Total value of %d products sold is $%.2f" %(total_sold,total_price))
		

# Return retail price of product ID
def retail_price(id):
	price = 0
	if(id==1):
		price = 2.98
	if(id==2):
		price = 4.50
	if(id==3):
		price = 9.98
	if(id==4):
		price = 4.49
	if(id==5):
		price = 6.87
	return price
		
		
# Call main function
main()