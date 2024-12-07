#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range (2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range (6, 21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


# all Test Case Passed
# Test case 0

# Test case 1

# Test case 2

# Test case 3

# Test case 4

# Test case 5

# Test case 6

# Test case 7
