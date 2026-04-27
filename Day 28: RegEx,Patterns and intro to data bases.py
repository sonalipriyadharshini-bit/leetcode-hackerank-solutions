#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    
    # List to store names that match the criteria
    names = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        # Check if email ends with @gmail.com
        if re.search(r"@gmail\.com$", emailID):
            names.append(firstName)

    # Sort names alphabetically
    names.sort()

    # Print each sorted name
    for name in names:
        print(name)
