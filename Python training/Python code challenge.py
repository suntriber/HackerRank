# From Facebook group Python

wrong_names = ['Yrret ,Maharg, Nhoj,Yrret, Leahcim ,Cire']

# output
# Correct names are: Eric, Michael, Terry, John, Graham, Terry

# wrong_names[0] = wrong_names[0].replace(' ', '')

# names = [n[::-1].capitalize() for n in wrong_names[0].replace(' ', '').split(',')]

print(f"Correct names are: {', '.join([n[::-1].capitalize() for n in wrong_names[0].replace(' ', '').split(',')])}")



# print out the reverse of the number with each digit doubled
# example 426 -> (reverse) 624 -> (double) 1248

# output
# The twisted numbers are: 86, 684, 181012, 14210, 16, 148

numbers = [34, 243, 659, 517, 8, 47]

print(f'The twisted numbers are: {", ".join(w for w in ["".join([str(int(c)*2) for c in str(n)[::-1]]) for n in numbers])}')



# You have a list of all small shoes in your small store [[model, size]]
# sort and print list of all shoes by model and size

shoes =[['B',9],['A',8],['A',7],['C',9],['A',9],['B',7],['C',8],['B',8]]

# output
"""
Sorted shoes:
A - 7
A - 8
A - 9
B - 7
B - 8
B - 9
C - 8
C - 9
"""

for i in sorted(shoes, key = lambda s: s[0]+str(s[1])):print(*i, sep=' - ')

# print(f"Sorted shoes:\n{(i for i in sorted(shoes, key = lambda s: s[0]+str(s[1])))}", sep=' - ')
