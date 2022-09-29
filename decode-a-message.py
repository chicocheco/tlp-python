"""
A message has been encoded as a text stream that is to be read character by character.
The stream contains a series of comma-delimited integers, each a positive number
capable of being represented by a C++ int.
However, the character represented by a particular integer depends on the current decoding mode.
There are three modes:
uppercase, lowercase, and punctuation.

In uppercase mode, each integer represents an uppercase letter: The integer
modulo 27 indicates the letter of the alphabet (where 1 = A and so on). So an input
value of 143 in uppercase mode would yield the letter H because 143 modulo 27 is
8 and H is the eighth letter in the alphabet.

The lowercase mode works the same but with lowercase letters; the remainder of
dividing the integer by 27 represents the lowercase letter (1 = a and so on). So an
input value of 56 in lowercase mode would yield the letter b because 57 modulo 27
is 2 and b is the second letter in the alphabet.

In punctuation mode, the integer is instead considered modulo 9, with the interpretation given by Table 2-3 below.
So 19 would yield an exclamation point because 19 modulo 9 is 1.

At the beginning of each message, the decoding mode is uppercase letters.
Each time the modulo operation (by 27 or 9, depending on mode) results in 0, the decoding mode switches.
If the current mode is uppercase, the mode switches to lowercase letters.
If the current mode is lowercase, the mode switches to punctuation, and if it is punctuation,
it switches back to uppercase.

EXAMPLE:
    Input
    18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10
    Output
    Right? Yes!
"""

# converting characters to integers
# this is only relevant in C++
# PROBLEM: READING A NUMBER WITH THREE OR FOUR DIGITS, FURTHER SIMPLIFIED
"""Write a program to read a number character by character and convert it to an inte-
ger, using just one char variable and two int variables. The number will have either
three or four digits."""
# digitChar == 10 means you input end-of-line, enter, empty space
"""
cout << "Enter a three-digit or four-digit number: ";
char digitChar = cin.get();
int threeDigitNumber = (digitChar - '0') * 100;
int fourDigitNumber = (digitChar - '0') * 1000;
digitChar = cin.get();
threeDigitNumber += (digitChar - '0') * 10;
fourDigitNumber += (digitChar - '0') * 100;
digitChar = cin.get();
threeDigitNumber += (digitChar - '0');
fourDigitNumber += (digitChar - '0') * 10;
digitChar = cin.get();
if (digitChar == 10) {
    cout << "Numbered entered: " << threeDigitNumber << "\n";
} else {
    fourDigitNumber += (digitChar - '0');
cout << "Numbered entered: " << fourDigitNumber << "\n";
}
"""
# now fix it to use only 1 int variable
"""
cout << "Enter a three-digit or four-digit number: ";
char digitChar = cin.get();
int number = (digitChar - '0') * 100;
digitChar = cin.get();
number += (digitChar - '0') * 10;
digitChar = cin.get();
number += (digitChar - '0');
digitChar = cin.get();
if (digitChar == 10) {
    cout << "Numbered entered: " << number << "\n";
} else {
    number = number * 10 + (digitChar - '0');
    cout << "Numbered entered: " << number << "\n";
}
"""
# expand it to handle more digits
"""
cout << "Enter a number with as many digits as you like: ";
char digitChar = cin.get();
int number = (digitChar - '0');
digitChar = cin.get();
while (digitChar != 10) {
    number = number * 10 + (digitChar - '0');
    digitChar = cin.get();
}
cout << "Numbered entered: " << number << "\n";
"""

# Python version where you input entire message at once
from string import ascii_uppercase, ascii_lowercase

dict_upper = {i: v for i, v in enumerate(ascii_uppercase, start=1)}
dict_lower = {i: v for i, v in enumerate(ascii_lowercase, start=1)}
dict_pun = {i: v for i, v in enumerate('!?,. ;"\'', start=1)}

# msg = input('Enter encoded message: ')
encoded_msg = '18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10'
# decoded: Right? Yes!

# Each time the modulo operation (by 27 or 9, depending on mode) results in 0, the decoding mode switches.
# UPPERCASE > LOWERCASE > PUNCTUATION and repeat
mode = 'UPPERCASE'
lst_msg = [int(i) for i in encoded_msg.split(',')]
for i in lst_msg:
    if mode == 'UPPERCASE':
        result = i % 27
        if result == 0:
            mode = 'LOWERCASE'
            continue
        print(dict_upper[result])
    elif mode == 'LOWERCASE':
        result = i % 27
        if result == 0:
            mode = 'PUNCTUATION'
            continue
        print(dict_lower[result])
    elif mode == 'PUNCTUATION':
        result = i % 9
        if result == 0:
            mode = 'UPPERCASE'
            continue
        print(dict_pun[result])
