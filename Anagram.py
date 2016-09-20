# Charlene Shu, Omar Olivarez, Kenneth Chow
# Program to check if two strings are anagrams

#Define main function
def main():
	#get input
	string1 = input("Input the first string you want to check for anagram: ")
	string2 = input("Input the second string you want to check for anagrams: ")
	#check if they are indeed anagrams
	if(isAnagram(string1, string2)):
		print("They are anagrams")
	else:
		print("They are not anagrams")

#checks if the two strings given have the same letters
def isAnagram(string1, string2):
	list_string2 = list(string2)
	#deletes each character in the string if they match
	if(len(string1) != len(string2)):
		return False
	for char in string1:
		for char2 in list_string2:
			if(char == char2):
				list_string2.remove(char)
	if(len(list_string2)==0):
		return True
	else:
		return False
main()
