"""
Print all possible permutations if sum(array) != n
"""

if __name__ == "__main__":
    x, y, z, n = 1, 1, 2, 3

    #xl, yl, zl = [i for i in range(x+1)], [i for i in range(y+1)], [i for i in range(z+1)]

    #total = [[i, j, k] for i in xl for j in yl for k in zl if sum([i, j, k]) != n]

    #print(total)

    print([[i, j, k] for i in [i for i in range(x+1)] for j in [i for i in range(y+1)] for k in [i for i in range(z+1)] if sum([i, j, k]) != n])