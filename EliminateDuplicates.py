# Charlene Shu, Omar Olivarez, Kenneth Chow
#Elimitates the duplicates of a list of numbers

def main():
	#gets user input
	user_input = ' '
	list_a = []
	#saves a list of the user inputs
	while user_input != 'q':
		user_input = input("Enter value for a list, use q to quit: ")
		if(user_input != 'q'):
			list_a.append(user_input)
	eliminateDuplicates(list_a)
	#eliminates the duplicates
def eliminateDuplicates(list_a):
	for num in list_a:
		i = list_a.index(num)+1
		while i < len(list_a):
			if(num == list_a[i]):
				del list_a[i]
			i+=1
	#prints the list
	print(list_a)
main()