"""
https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
"""

def solution(S):
    s = S[0]
    for i in range(1, len(S)):
        if S[i] == s[-1]:
            s += S[i]
        else:
            print(f'({len(s)}, {int(s[0])}) ',end='')
            s = S[i]
    print(f'({len(s)}, {int(s[0])})',end='')



if __name__ == "__main__":
    solution('1222311')  # should print (1, 1) (3, 2) (1, 3) (2, 1)