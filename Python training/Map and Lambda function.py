"""
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
"""

cube = lambda x: x**3

def fibonacci(n):
    l = []
    
    for i in range(n):
        l.append(fib(i))
    return l

        
def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

if __name__ == '__main__':
    # n = int(input())
    n = 5
    print(list(map(cube, fibonacci(n))))


