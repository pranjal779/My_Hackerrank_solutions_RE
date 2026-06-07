#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    # Python If-Else
    # check if the number is odd
    if n % 2 != 0:
        print("Weird")
    else:
        # If the number is even, evaluate the specific ranges
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n> 20:
            print("Not Weird")
