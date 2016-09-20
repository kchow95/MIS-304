# Charlene Shu, Omar Olivarez, Kenneth Chow
#Program to write user input of majors and codes to majors.txt

def main():

	#opens the file
	outfile = open("majors.txt", 'w')
	code = ''
	#gets user input until they want to stop
	while(code != 'n'): 
		code = input("Give a six digit code of the major or n to stop: ")
		if(code == 'n'):
			break
		description = input("Give a description of the major: ")
		outfile.write(code)
		outfile.write(' ')
		outfile.write(description)
		outfile.write('\n')
	#Close the output file
	outfile.close()

main()
