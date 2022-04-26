"""
Passing Cars
Count the number of passing cars on the road.

A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of 
array A represent consecutive cars on a road.
Array A contains only 0s and/or 1s:
        0 represents a car traveling east,
        1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 <= P < Q < N, is passing when P is
traveling to the east and Q is traveling to the west.
For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
Write a function:
    int solution(int A[], int N);
that, given a non-empty zero-indexed array A of N integers, returns the number of pairs of passing cars.
The function should return -1 if the number of pairs of passing cars exceeds 1,000,000,000.
For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.
Assume that:
        N is an integer within the range [1..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.
Complexity:
        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

MAX_INT = int(100000)
MAX_PAIRS = int(1e9)


def solution(A):
    """
    :param A: array of int (0 or 1 which are actually booleans)
    :return: integer count of pairs of passing cars, or -1 if more than 1e9 pairs
    """
    east = 0
    pairs = 0
    for car in A:
        if not car:
            east += 1
        else:
            pairs += east
        if pairs > MAX_PAIRS:
            return -1
    return pairs


if __name__ == "__main__":
        print(f'{solution([0, 0, 0, 0])} --> 0' if not solution([1, 1, 1, 1]) else f'ERRRRROR')
        print(f'{solution([0, 0, 0, 1])} --> 3' if not solution([1, 1, 1, 1]) == 3 else f'ERRRRROR')
        print(f'{solution([0, 0, 1, 1])} --> 4' if not solution([1, 1, 1, 1]) == 4 else f'ERRRRROR')
        print(f'{solution([0, 1, 0, 0])} --> 1' if not solution([1, 1, 1, 1]) == 1 else f'ERRRRROR')
        print(f'{solution([0, 1, 0, 1])} --> 3' if not solution([1, 1, 1, 1]) == 3 else f'ERRRRROR')
        print(f'{solution([0, 1, 1, 1])} --> 3' if not solution([1, 1, 1, 1]) == 3 else f'ERRRRROR')
        print(f'{solution([1, 0, 0, 0])} --> 0' if not solution([1, 1, 1, 1]) else f'ERRRRROR')
        print(f'{solution([1, 0, 0, 1])} --> 2' if not solution([1, 1, 1, 1]) == 2 else f'ERRRRROR')
        print(f'{solution([1, 0, 1, 0])} --> 1' if not solution([1, 1, 1, 1]) == 1 else f'ERRRRROR')
        print(f'{solution([1, 0, 1, 1])} --> 2' if not solution([1, 1, 1, 1]) == 2 else f'ERRRRROR')
        print(f'{solution([1, 1, 0, 0])} --> 0' if not solution([1, 1, 1, 1]) else f'ERRRRROR')
        print(f'{solution([1, 1, 0, 1])} --> 1' if not solution([1, 1, 1, 1]) == 1 else f'ERRRRROR')
        print(f'{solution([1, 1, 1, 0])} --> 0' if not solution([1, 1, 1, 1]) else f'ERRRRROR')
        print(f'{solution([1, 1, 1, 1])} --> 0' if not solution([1, 1, 1, 1]) else f'ERRRRROR')