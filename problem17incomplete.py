"""
one two ... twenty nine, then first number changes so go to thirty?

look at number of digits in number, first word is then obvious i think,
minus that number from number and repeat? need to stick ands in after hundreds always

"""


numberwords = {   1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def numtoword(n):
    word=''
    thousandcount=0
    while n>=1000:
        thousandcount+=1
        n-=1000
    word+=numberwords[thousandcount]+'thousand'

    hundredcount=0
    while n>=100:
        hundredcount+=1
        n-=100
    word+=numberwords[hundredcount]+'hundred'

    tencount=0
    while n>=10:
        tencount+=1
        n-=10
    word+=numberwords[10*tencount]
    word+=numberwords[n]
    return word

print(numtoword(1444))
