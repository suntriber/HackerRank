"""
https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
"""

"""
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""

def logo(s):
    from collections import Counter
    
    _list = sorted([s.count(c) for c in set(s)], reverse=True)
    
    _chars = []
    for n in _list:
        for c in sorted(s):
            if s.count(c) == n:
                if c not in _chars: _chars.append(c)
    
    
    return ''.join(c for c in _chars[:3])
    
    
    


if __name__ == "__main__":
    print(f"GOE --> {logo('GOOGLE')}")
    print(f"bac --> {logo('aabbbccde')}")

    