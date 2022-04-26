"""
https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
"""

# n, m = input().split()


# arr = input().split()
arr = "1 5 7"

# A = set(input().split())
# B = set(input().split())
A = {'1', '3', '7'}
B = {'2', '4', '5'}


print(sum([(i in A) - (i in B) for i in arr]))
print([(i in A) - (i in B) for i in arr])

for i in arr:
    print(i in A)
    print(i in B)
    print(((i in A) - (i in B)))