"""
https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
"""

def split_and_join(line):
    return line.replace(' ', '-')


if __name__ == "__main__":
    print(split_and_join("this is a string"))