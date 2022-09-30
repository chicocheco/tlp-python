"""Alternative to luhn checksum script.
Take a 13-digit ISBN without its check digit (so 12 digits) and generate the check digit."""
import sys


def double_digit_value(digit: int):
    doubled_digit = digit * 2
    if doubled_digit >= 10:
        return 1 + (doubled_digit % 10)
    return doubled_digit


# example of ISBN-13: 978-0-306-40615-7
# 978030640615
# check digit calculated using luhn formula is: 6
# check digit calculated using isbn formula is: 7

# other examples:
# 978-1-59327-424-5, 978-1-56619-909-4

number = [int(digit) for digit in input('Enter first 12 digits of 13-digit ISBN number to generate the check digit: ')]

if len(number) != 12:
    print('Not 12 digits.')
    sys.exit()

isbn_sum = 0
luhn_sum = 0
for i, digit in enumerate(number, start=1):
    if i % 2 == 0:
        isbn_sum += digit * 3  # https://en.wikipedia.org/wiki/ISBN
        luhn_sum += double_digit_value(digit)
    else:
        isbn_sum += digit
        luhn_sum += digit

print(f'LUHN: Checksum of {luhn_sum} digits is {str(10 - (luhn_sum % 10))[-1]}.')
print(f'ISBN (real use): Checksum of {isbn_sum} digits is {str(10 - (isbn_sum % 10))[-1]}.')
