"""
https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def detect_float(n):
    if '.' not in n or n[-1] == '.':
        return False
    else:
        return isfloat(n)



if __name__ == "__main__":
    print(f"{detect_float('+4.50')} --> True")
    print(f"{detect_float('-1.0')} --> True")
    print(f"{detect_float('.5')} --> True")
    print(f"{detect_float('-.7')} --> True")
    print(f"{detect_float('+.4')} --> True")

    print(f"{detect_float('-+4.5')} --> False")
    print(f"{detect_float('12.')} --> False")
    print(f"{detect_float('12.0')} --> True")

    
""" Reading test cases from stdin
for i in range(int(input())):    
    try:
        n=input()
        print(detect_float(n))
    except:        
        print('False')
"""