#!/usr/bin/env python3

# Import sys to handle command-line arguments
import sys

# Verify that there are exactly 2 arguments given
if len(sys.argv) != 3:
    # Print the message and depart if 2 arguments are not given
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Signal successful exit, even though it's an error in context

# Provide the appropriate command-line arguments to the variables
name = sys.argv[1]  # First argument
age = int(sys.argv[2])  # Second argument (convert to integer)

# Print the message 
print(f'Hi {name}, you are {age} years old.')


    
