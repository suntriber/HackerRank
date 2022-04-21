"""
https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
"""

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta
import time

from numpy import datetime_as_string

# Complete the time_delta function below.
def time_delta(t1, t2):

    months = {'Jan' : '1', 'Feb' : '2', 'Mar' : '3', 'Apr' : '4', 'May' : '5', 'Jun' : '6',
              'Jul' : '7', 'Aug' : '8', 'Sep' : '9', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12'}

    const1 = t1.split(' ')[-1]
    const2 = t2.split(' ')[-1]

    d1 = t1.split(' ')[1:-1]
    d1[1] = months[d1[1]]
    dt1 = datetime(int(d1[2]), int(d1[1]), int(d1[0]), int(d1[3].split(':')[0]), int(d1[3].split(':')[1]), int(d1[3].split(':')[2]))
    

    d2 = t2.split(' ')[1:-1]
    d2[1] = months[d2[1]]
    dt2 = datetime(int(d2[2]), int(d2[1]), int(d2[0]), int(d2[3].split(':')[0]), int(d2[3].split(':')[1]), int(d2[3].split(':')[2]))
    

    const1 = [n for n in const1]
    const2 = [n for n in const2]

    const1 = [const1[0], int(''.join(n for n in const1[1:3]))*3600, int(''.join(n for n in const1[3::]))*60]
    const2 = [const2[0], int(''.join(n for n in const2[1:3]))*3600, int(''.join(n for n in const2[3::]))*60]

    const1 = sum(const1[1:]) if const1[0]=='+' else -sum(const1[1:])
    const2 = sum(const2[1:]) if const2[0]=='+' else -sum(const2[1:])


    # print(f'Diff t1-t2 = {(dt1-dt2).total_seconds()}')
    # print(f'Diff c1-c2 = {const1-const2}')



    return str(int(abs(((dt1-dt2).total_seconds()) - (const1 - const2))))
    

if __name__ == "__main__":

    print(f"{time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000')} -> 25200")
    print(f"{time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000')} -> 88200")
    