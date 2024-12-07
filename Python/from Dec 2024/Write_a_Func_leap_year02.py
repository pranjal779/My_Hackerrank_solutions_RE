def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            leap = True

    return leap

year = int(input())
print(is_leap(year))

# 2/6 test cases failed :(

# Test case 1 X

# Test case 5 X

# Test case 0

# Test case 2

# Test case 3

# Test case 4
# Compiler Message
# Wrong Answer
