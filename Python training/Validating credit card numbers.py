"""
https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
"""
import re


def validate(card):

    if re.findall('[^\d\-]', card):
        return 'Invalid'
    elif len([c for c in card if c.isdigit()]) != 16:
        return 'Invalid'
    elif card[0] not in '456':
        return 'Invalid'
    elif has_consecutive(card):
        return 'Invalid'
    elif '-' in card and card.count('-') != 3 and (len(card.split('-')[0])%4 + len(card.split('-')[1])%4 + len(card.split('-')[2])%4 + len(card.split('-')[3])%4) != 0:
        return 'Invalid'
    
    return 'Valid'


def has_hyphen(str):
    pass

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


def refind(s):
    return False if re.findall('[^\d\-]', s) else True



    


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

    # for c in cards:
    #     print(validate(c))

    print('-'*35)

    cards2 = ['7165863385679329',
    '6175824393389297',
    '5252248277877418',
    '9563584181869815',
    '5179123424576876']

    # for c in cards2:
    #     print(validate(c))

    # print("OK" if not refind('5123 - 3567 - 8912 - 3456') else "ERROR")
    # print("OK" if refind('5133-3367-8912-3456') else "ERROR")
    # print("OK" if not refind("44244x4424442444") else "ERROR")


    # print("OK" if not has_consecutive("1234-4465-6667-8899") else "ERROR")

    # n = "44244x4424442444"
    # n = "0525362587961578"
    n = '6123-4567-8912-3456'

    print("YES" if re.match(r'(\d{4}-){3}\d{4}$', n) or re.match(r'\d{16}$', n) else "NO")

    print(n)
    n = re.sub(r'-', '', n)

    print(n)
    



    """
    import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")
    """


    """
    def validate_credit_cards(credit_cards):
    valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
    no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
    filters = valid_structure, no_four_repeats

    for cc in credit_cards:
        if all(re.match(f, cc) for f in filters):
            print("Valid")
        else:
            print("Invalid")
    """


    """
    import re

for _ in range(int(input())):
    n = input().strip()
    try:
        assert re.match(r'(\d{4}-){3}\d{4}$', n) or re.match(r'\d{16}$', n) # total digits == 16 and groups of four if split by '-'
        n = re.sub(r'-', '', n)  # remove all '-' from string
        assert re.match(r'[456]', n)
        assert not re.search(r'(\d)\1{3,}', n)
    except:
        print('Invalid')
    else:
        print('Valid')
    """
