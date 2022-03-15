"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example:

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""

#records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
records = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]

second_lowest = set([x[1] for x in records])
second_lowest = sorted(list(second_lowest))

st = []

for s in records:
    if s[1] == second_lowest:
        st.append(s[0])

for s in sorted(st):
    print(s)

print(second_lowest)