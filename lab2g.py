#!/usr/bin/env python3

# Author: Joy Otchere
# Author ID: JoyOtchere
# Date Created: 2024/09/26

# Import sys to manage the command-line arguments
import sys

# Check if an argument was given, instead set the timer to 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the argument as timer
else:
    timer = 3  # Default value for the timer

# While loop that runs until timer equals 0
while timer > 0:
    print(timer)  # Print the current timer value
    timer -= 1    # Decrease the timer by 1

print("blast off!")  # Print the final message
