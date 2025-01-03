import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Congratulations!

# You have passed the sample test cases. Click the submit button to run your code against all the test cases.


# Sample Test case 0


# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:
# - string string: a long string
# - int max_width: the width to wrap to

# Returns:
# string: a single string with newline characters ('\n') where the breaks should be

# Input Format

# The first line contains a string, string.
# The second line contains the width, max width.

# Constraints
# - 0 < len(string) <1000
# - 0 < max width < len(string)

# Sample Input 0
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4


# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


# tutorial
# Textwrap
# The textwrap module provides two convenient functions: wrap() and fill().

# textwrap.wrap()
# The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
# It returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
# Output:
# ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
# textwrap.fill()
# The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)

# Output:
# This is
# a very
# very
# very
# very
# very
# long
# string.

# test case 1:
# Compiler Message
# Success
# Input (stdin)
# bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd
# 9
# Expected Output
# bscnksbcj
# scksbcjks
# bckjdscsb
# dcbsdkjbc
# sdjcbsdjk
# cbsdkjbck
# jdsbjksd

# # test case 2:
# Compiler Message
# Success
# Input (stdin)
# bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd
# 20
# Expected Output
# bscnksbcjscksbcjksbc
# kjdscsbdcbsdkjbcsdjc
# bsdjkcbsdkjbckjdsbjk
# sd

# # test case 3:
# Compiler Message
# Success
# Input (stdin)
# bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd
# 11
# Expected Output
# bscnksbcjsc
# ksbcjksbckj
# dscsbdcbsdk
# jbcsdjcbsdj
# kcbsdkjbckj
# dsbjksd

# # test case 4:
# Compiler Message
# Success
# Input (stdin)
# bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd
# 15
# Expected Output
# bscnksbcjscksbc
# jksbckjdscsbdcb
# sdkjbcsdjcbsdjk
# cbsdkjbckjdsbjk
# sd

# # test case 5:
# Compiler Message
# Success
# Input (stdin)
# bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjd
# 15
# Expected Output
# bscnksbcjscksbc
# jksbckjdscsbdcb
# sdkjbcsdjcbsdjk
# cbsdkjbckjd
