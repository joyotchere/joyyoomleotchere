#!/usr/bin/env python3

#Import sys to handle command-line arguments
import sys


#Provide the appropriate command-line arguments to the variables
name = sys.argv[1]  # First argument
age = int(sys.argv[2])  # Second argument (convert to integer)


#Print the message
print('Hi ' + name + ', you are ' + str(age) + ' years old.')

