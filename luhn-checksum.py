"""
The Luhn formula is a widely used system for validating identification numbers. Using
the original number, double the value of every other digit. Then add the values of the
individual digits together (if a doubled value now has two digits, add the digits indi-
vidually). The identification number is valid if the sum is divisible by 10.
Write a program that takes an identification number of arbitrary length and
determines whether the number is valid under the Luhn formula. The program must
process each character before reading the next one.
"""

# breaking down the problem, a list:
# knowing which digits to double
# treating doubled numbers 10 and greater according to their individual digits
# knowing we've reached the end of the number
# reading each digit separately


# PROBLEM: treating doubled numbers 10 and greater according to their individual digits
digit = int(input('Enter a single digit number, 0-9: '))
doubled_digit = digit * 2

if doubled_digit >= 10:
    # if the doubled value is 10 or greater, then it must be in the range 10–18, and therefore the first digit is 1
    summary = 1 + (doubled_digit % 10)
else:
    summary = doubled_digit

print('Sum of digits in doubled number: ', summary)


# make a function from it
def double_digit_value(digit: int):
    doubled_digit = digit * 2
    if doubled_digit >= 10:
        return 1 + (doubled_digit % 10)
    return doubled_digit


# PROBLEM: reading each digit separately
# (more like C++ problem but kept for clarity because in Python you use int() when reading input)
# important: string '0' in C++ translates to 48 when reading cin
"""
char digit;
cout << "Enter a one-digit number: ";
cin >> digit;
int sum = digit - '0';
cout << "Is the sum of digits " << sum << "? \n";
"""

# PROBLEM: knowing which digits to double
# problem reduction 1: luhn checksum validation, fixed length
# problem reduction 2: simple checksum validation, fixed length
# (read the digits, sum them, determine whether the sum is divisible by 10)
print('Enter a six-digit number: ')

checksum = 0
for i in range(6):
    digit = int(input())
    checksum += digit

print(f'Checksum is {checksum}.')
if checksum % 10 == 0:
    print('Checksum is divisible by 10. Valid.')
else:
    print('Checksum is NOT divisible by 10. Invalid.')

# From here, we need to add the logic for the actual Luhn validation formula,
# which means doubling every other digit starting from the second digit from the right (skipping CHECK DIGIT)

# problem reduction 1: luhn checksum validation, fixed length
print('Enter a six-digit number: ')

checksum = 0
for pos in range(1, 7):  # 1 through 6
    digit = int(input())
    # given 6 digits, double only every odd digit
    if pos % 2 == 0:
        checksum += digit
    else:
        checksum += double_digit_value(digit)

print(f'Checksum is {checksum}.')
if checksum % 10 == 0:
    print('Checksum is divisible by 10. Valid.')
else:
    print('Checksum is NOT divisible by 10. Invalid.')

# problem reduction 1: luhn checksum validation, arbitrary length
# switch over to while loop, break out when not input

# print('Enter a number with an even number of digits (stop by pressing enter): ')
checksum = 0
position = 1
while True:
    inp = input()
    if not inp:
        break
    digit = int(inp)
    # given number with even number of digits, double only every odd digit
    if position % 2 == 0:
        checksum += digit
    else:
        checksum += double_digit_value(digit)
    position += 1

print(f'Checksum is {checksum}.')
if checksum % 10 == 0:
    print('Checksum is divisible by 10. Valid.')
else:
    print('Checksum is NOT divisible by 10. Invalid.')

# How do I know the length of the number when it's not predefined?
# Count both odd and even numbers!

# create an analogy first:
positive_count = 0
negative_count = 0
for i in range(10):
    number = int(input())
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

inp = input('Do you want the (p)ositive or (n)egative count? ').lower()
if inp == 'p':
    print(f'Positive count is {positive_count}.')
elif inp == 'n':
    print(f'Negative count is {negative_count}.')
# now move one back to our problem:

print('Enter a number (stop by pressing enter): ')
odd_length_checksum = 0
even_length_checksum = 0
position = 0
while True:
    inp = input()
    if not inp:
        break
    position += 1  # or subtract 1 from position when loop finished...
    digit = int(inp)
    # do both checksums at once, there are only 2 possibilities anyway!
    if position % 2 == 0:
        even_length_checksum += digit
        odd_length_checksum += double_digit_value(digit)
    else:
        even_length_checksum += double_digit_value(digit)
        odd_length_checksum += digit

if position % 2 == 0:
    checksum = even_length_checksum
else:
    checksum = odd_length_checksum

print(f'Checksum of {position} digits is {checksum}.')
if checksum % 10 == 0:
    print('Checksum is divisible by 10. Valid.')
else:
    print('Checksum is NOT divisible by 10. Invalid.')
