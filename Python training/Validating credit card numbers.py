"""
https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
"""

def validate(card):
    import re
    if len([c for c in card if c.isdigit()]) != 16:
        return 'Invalid'
    elif card[0] not in '456':
        return 'Invalid'
    elif re.findall('[^\d\-]', card):
        return 'Invalid'
    elif has_consecutive(card):
        return 'Invalid'
    elif '-' in card:
        if len(card.split('-')[0])!=4 or len(card.split('-')[1])!=4 or len(card.split('-')[2])!=4 or len(card.split('-')[3])!=4:
            return 'Invalid'
    
    return 'Valid'


def has_consecutive(str):
    str = ''.join(c for c in str if c!='-')
    for i in range(len(str)-1):
        tmp = str[i]
        j = i+1
        if (j+2 <= (len(str)-1)) and str[j] == tmp:
            if str[j+1] == tmp:
                if str[j+2] == tmp:
                    return True
    return False



    


if __name__ == "__main__":
    # print(f'{validate("42536258796157867")} --> INVALID')       #17 digits in card number → Invalid 
    # print(f'{validate("4424444424442444")} --> INVALID')        #Consecutive digits are repeating 4 or more times → Invalid
    # print(f'{validate("5122-2368-7954 - 3214")} --> INVALID')   #Separators other than '-' are used → Invalid
    # print(f'{validate("44244x4424442444")} --> INVALID')        #Contains non digit characters → Invalid
    # print(f'{validate("0525362587961578")} --> INVALID')        #Doesn't start with 4, 5 or 6 → Invalid

    # print(has_consecutive('aaa'))
    cards = ['4123456789123456',
    '5123-4567-8912-3456',
    '61234-567-8912-3456',
    '4123356789123456',
    '5133-3367-8912-3456',
    '5123 - 3567 - 8912 - 3456']

    for c in cards:
        print(validate(c))
    # print(validate('5123-4567-8912-3456'))
    # print(has_consecutive('5133-3367-8912-3456'))
    