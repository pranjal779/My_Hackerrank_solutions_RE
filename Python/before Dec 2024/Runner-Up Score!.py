# Find the Runner-Up Score!

# Given the participants
# scoresheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format
#
# The first line contains . The second line contains an array A[] of n integers each separated by a space.
# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100
#
# Output Format
#
# Print the runner-up score.
#
# Sample Input 0
# 5
# 2 3 6 6 5
# Sample output 0
# 5
# Explanation 0
# Given list [2, 3, 6, 6, 5]. the maximum score is 6, second maximum is 5. hence, we print 5 as the runner-up score.
n = int(input())

nums = map(int, input().split())
print(sorted(list(set(nums)))[-2])
