# Charlene Shu, Omar Olivarez, Kenneth Chow
# computes the stats based on scores and majors txt

import math

def main():
	infile = open("scores.txt", "r")
	outfile = open("results.txt", "w")

	for line in infile:
		student_list_scores = line.split()
		outfile.write(student_list_scores[0] + " ")
		str1 = ''
		for word in get_major(student_list_scores[1]):
			str1 += word 
			str1+=' '
		outfile.write(str1+ ' ')
		outfile.write(str(min(student_list_scores[2:]))+ " ")
		outfile.write(str(max(student_list_scores[2:]))+ " ")
		outfile.write("{0:.2f}".format(mean(student_list_scores[2:]))+ " ")
		outfile.write("{0:.2f}".format(standard_dev(student_list_scores[2:]))+ "\n")

	infile.close()
	outfile.close()
#Compute the max by comparing numbers
def max(scores):
	max1 = 0.0
	for num in scores:
		if float(num) > max1:
			max1 = float(num)
	return max1
#Compute the min by comparing numbers
def min(scores):
	min1 = 100.0
	for num in scores:
		if float(num) < min1:
			min1 = float(num)
	return min1
#gets the major by comaparing the code to the majors.txt file
def get_major(code):
	infile_majors = open("majors.txt", "r")
	for line in infile_majors:
		major = line.split()
		if major[0] == code:
			return major[1:]
#returns the standard deviation of the scores
def standard_dev(scores):
	total = 0.0
	average = mean(scores)
	for num in scores:
		total += (float(num) - average)**2
	standard_dev = math.sqrt(total/(len(scores)-1))
	return standard_dev
#returns the mean of the scores
def mean(scores):
	total = 0.0
	count = 0
	for num in scores:
		total += float(num)
	average = total/len(scores)
	return average

main()
