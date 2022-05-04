"""
https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
"""

import cmath
c = complex(input())
print((c.real**2 + c.imag**2)**0.5)
print(cmath.phase(c))