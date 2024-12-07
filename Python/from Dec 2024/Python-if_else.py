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
    if n % 2 == 0 and n in range (2, 5):
        print("Not Weird")
    if n % 2 == 0 and n in range (6, 20):
        print("Weird")
    if n % 2 == 0 and n > 20:
        print("Not Weird")


# 1/8 test cases failed :(

# Test case 7 X (this case was failed)

# Test case 0 

# Test case 1

# Test case 2

# Test case 3

# Test case 4

# Test case 5

