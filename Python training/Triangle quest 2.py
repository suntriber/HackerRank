"""
https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true
"""

if __name__ == "__main__":
    N = 7

    for i in range(1, N+1):

        # print(*[n for n in range(1,i+1)]+[n for n in range(1,i)[::-1]], sep='')
        print(((10**i - 1)//9)**2)