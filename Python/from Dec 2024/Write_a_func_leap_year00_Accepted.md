# Working version:
```python
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap

year = int(input())
print(is_leap(year))
```

# Non-Working Version:
```py
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        leap = True  # This line is problematic.

    return leap

year = int(input())
print(is_leap(year))
```

or
```py
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            leap = False
        leap = True
    leap = False
```

### context:
As
only year % 4 == 0 is needed
and otherwise year % 100 != 0 (should not be equal to zero) unless Divisiable by 400

Divisible by 4.
Not divisible by 100 (unless also divisible by 400).

Explanation:
Working Version:

In the working version, the code structure follows this logic:
If year % 4 == 0, it checks the next condition (year % 100 == 0).
If year % 100 == 0, it checks whether year % 400 == 0. If true, leap = True.
If year % 100 != 0, leap = True is set directly without checking divisibility by 400 because it's still a valid leap year (divisible by 4 but not by 100).
The key here is that leap = True is only set when necessary, and the flow of logic works as intended based on the calendar rules for leap years.

Non-Working Version:

In the non-working version, the line leap = True is incorrectly placed outside the if year % 100 == 0 block, but still inside the if year % 4 == 0 block.
This means that for any year divisible by 4, the code will always set leap = True regardless of whether it is divisible by 100 or 400.
Specifically, if a year is divisible by 4 but not divisible by 100 (like 1990), this line will still incorrectly set leap = True, which is wrong because 1990 is not a leap year.
Why the Non-Working Version is Incorrect:
The placement of leap = True in the second version causes it to be set even when the year is divisible by 4 but not by 100. The Gregorian calendar rule says that such years are not leap years, but the code mistakenly sets leap = True for these cases.

Correct Approach:
You should only set leap = True in the appropriate conditions where the year qualifies as a leap year. 
The working version correctly follows these rules, while the non-working version fails because it prematurely sets leap = True in cases where it shouldn't.


