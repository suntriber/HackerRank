"""
https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
"""

from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):


    dt1 = convert_to_dt(t1)
    dt2 = convert_to_dt(t2)

    const1 = convert_to_const(t1)
    const2 = convert_to_const(t2)

    return str(int(abs(((dt1-dt2).total_seconds()) - (const1 - const2))))
    

def convert_to_dt(time):
    months = {'Jan' : '1', 'Feb' : '2', 'Mar' : '3', 'Apr' : '4', 'May' : '5', 'Jun' : '6',
              'Jul' : '7', 'Aug' : '8', 'Sep' : '9', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12'}
    
    d1 = time.split(' ')[1:-1]
    d1[1] = months[d1[1]]
    return datetime(int(d1[2]), int(d1[1]), int(d1[0]), int(d1[3].split(':')[0]), int(d1[3].split(':')[1]), int(d1[3].split(':')[2]))
        

def convert_to_const(time):
    const1 = [n for n in time.split(' ')[-1]]
    const1 = [const1[0], int(''.join(n for n in const1[1:3]))*3600, int(''.join(n for n in const1[3::]))*60]
    return sum(const1[1:]) if const1[0]=='+' else -sum(const1[1:])


if __name__ == "__main__":

    print(f"{time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000')} -> 25200")
    print(f"{time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000')} -> 88200")
