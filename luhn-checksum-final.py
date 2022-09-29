"""The Luhn formula is a widely used system for validating identification numbers. Using
the original number, double the value of every other digit. Then add the values of the
individual digits together (if a doubled value now has two digits, add the digits individually).
The identification number is valid if the sum is divisible by 10.
Write a program that takes an identification number of arbitrary length and
determines whether the number is valid under the Luhn formula. The program must
process each character before reading the next one."""

def double_digit_value(digit: int):
    doubled_digit = digit * 2
    if doubled_digit >= 10:
        return 1 + (doubled_digit % 10)
    return doubled_digit


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
