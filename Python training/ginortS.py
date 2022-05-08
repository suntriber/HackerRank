"""
https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
"""
# s = input()
s = 'Sorting1234'

lc, uc, od , ed= '','','', ''

for c in s:
    if c.islower():lc+=c
    elif c.isupper():uc+=c
    elif c.isdigit():
        if int(c)%2:od+=c
        else:ed+=c

print(*(sorted(lc)+sorted(uc)+sorted(od)+sorted(ed)), sep='')


# print(lc)
# print(d)
# print(uc)