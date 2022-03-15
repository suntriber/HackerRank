"""
https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
"""

def merge_the_tools(string, k):

    split_string = [string[i:i+k] for i in range(0, len(string), k)]
    s = ''
    for e in split_string:
        for c in e:
            if c not in s:
                s+=c
        print(s)
        s = ''


if __name__ == "__main__":
    merge_the_tools('AABCAAADA', 3)