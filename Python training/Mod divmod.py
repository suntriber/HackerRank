"""
https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""

a, b = int(input()), int(input())

print(f"{a//b}\n{a%b}\n{divmod(a, b)}")