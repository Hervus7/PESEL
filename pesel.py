import random
import argparse

# Dictionaries used to decode century from month segment and vice versa
CENTURIES = {0: 19, 1: 20, 2: 21, 3: 22, 4: 18}
CENTURIES_REVERSED = {cent: num for num, cent in CENTURIES.items()}

# Mask used to calculate check digit
# Correct mask is actually 1379137913,
# but reversing it makes calculation less complicated
MASK = '9731973197'

def is_leap(year: int) -> bool:
    """ https://stackoverflow.com/a/30714165 """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def check_digit(pesel: str) -> int:
    """ Calculates check digit (the 11th one) basing on the first ten digits """
    return sum([int(c) * int(m) for c, m in zip(pesel[0:10], MASK)]) % 10

def is_valid(pesel: str) -> bool:
    """
    Checks if string is a valid PESEL. Criterias are:
    11 chars long,
    correct check digit,
    month and day are both not equal to 0 (makes '00000000000' invalid)
    """
    if len(pesel) == 11:
        if int(pesel[10]) == check_digit(pesel):
            if all([int(pesel[i*2:i*2+2]) for i in range(1, 3)]):
                return True
    return False

def is_female(pesel: str) -> bool:
    """
    The 10th digit determine gender
    odd - male
    even - female
    """
    return int(pesel[9]) % 2 == 0

def birth_date(pesel: str) -> list:
    """ Returns birth date from a PESEL """
    century, month = divmod(int(pesel[2:4]), 20)
    day = pesel[4:6]
    year = f'{CENTURIES.get(century)}{pesel[0:2]}'
    month = str(month).zfill(2)
    return day, month, year

def gen_pesel(day=None, month=None, year=None, female=None) -> str:
    """ Generates random valid PESEL """
    year = str(random.randint(1800, 2299)) if not year else str(year)
    month = random.randint(1, 12) if not month else int(month)
    max_day = 31 if month != 2 else 31-(2+int(not is_leap(int(year))))
    day = str(random.randint(0, max_day)).zfill(2) if not day else str(day)
    cent_month = str(CENTURIES_REVERSED.get(int(year[0:2]))*20+month).zfill(2)
    gender = random.randint(0, 9999)
    if female != None : gender = gender-gender%2 if female else gender-gender%2+1
    parts = year[2:4]+str(cent_month)+day+str(gender).zfill(4)
    parts += str(check_digit(parts))
    return parts

def show_info(pesel: str) -> None:
    """ Prints info in a nice way """
    gender = 'female' if is_female(pesel) else 'male'
    print('--- '+pesel+' ---')
    print('Valid : ', is_valid(pesel))
    print('Gender : ', gender)
    print('Birth date : day: {} month: {} year: {}'.format(*birth_date(pesel)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if string is a valid PESEL or generate random valid PESEL with specified parameters')
    parser.add_argument('pesel', nargs='?', help='check if string is a valid PESEL')
    parser.add_argument('-d', '--day', help='day of birth', required=False, type=str)
    parser.add_argument('-m', '--month', help='month of birth', required=False, type=str)
    parser.add_argument('-y', '--year', help='year of birth', required=False, type=str)
    parser.add_argument('-f', '--female', help='if gender has to be female (leave unchanged for random)', required=False, type=int, choices=[0, 1])
    args = parser.parse_args()

    pesel = args.pesel if args.pesel else gen_pesel(args.day, args.month, args.year, args.female)
    show_info(pesel)
