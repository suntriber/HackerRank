# From Facebook group Python

wrong_names = ['Yrret ,Maharg, Nhoj,Yrret, Leahcim ,Cire']

# output
# Correct names are: Eric, Michael, Terry, John, Graham, Terry

# wrong_names[0] = wrong_names[0].replace(' ', '')

# names = [n[::-1].capitalize() for n in wrong_names[0].replace(' ', '').split(',')]

print(f"Correct names are: {', '.join([n[::-1].capitalize() for n in wrong_names[0].replace(' ', '').split(',')])}")