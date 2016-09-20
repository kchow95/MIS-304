#Temperature Conversion project submission for Kenneth Chow, Omar Olivarez, and Charlene Shu


#program to convert temperature


#import the message box
import tkinter.messagebox
#call the main function
def main ():
    
    #declare the variables
    option = 0
    temp = 0.0
    cel = 0.0
    fahr = 0.0
    message = ""
    
    #Get user input
    option = int (input("Welcome to Temperature Conversion Program. \n1) Convert from Fahrenheit to Celsius. \n2) Convert from Celsius to Fahrenheit. \nEnter your choice: "))
    temp = (float(input("Enter the temperature: ")))
    
    #Convert F to C
    cel = (5.0/9.0) * (temp - 32)
    #Convert C to F
    fahr = (9.0/5.0) * temp + 32
    
    #declare the message
    if (option == 1):
        message = ("You selected Option 1.\n%.2f degrees Fahrenheit is equal to %.2f degrees Celsius." %(temp, cel))
    elif (option == 2):
        message = ("You selected Option 2. \n %.2f degrees Celsius is equal to %.2f degrees Fahrenheit" %(temp, fahr))
    
    #display the message:
    tkinter.messagebox.showinfo("Temperature Conversion", message)
    
#Run the main function
main()
