"""Write a program that reads a line of text, counting the number of words,
identifying the length of the longest word, the greatest number of vowels
in a word, and/or any other statistics you can think of."""
import re
from collections import defaultdict
from operator import itemgetter

sen = 'Write a program that reads a line of text, counting the number of words, ' \
      'identifying the length of the longest word, the greatest number of vowels ' \
      'in a word, and/or any other statistics you can think of.'

vowels = tuple('aeiouy')

lst_sen = [word for word in re.split(r'\W', sen) if word]
num_words = len(lst_sen)
print(f'Words counted: {num_words}.')

longest_word = max((len(word), word) for word in lst_sen)
length, word = longest_word[0], longest_word[1]
print(f'The longest word is "{word}": {length} letters.')

dict_vowels = defaultdict(int)
for word in lst_sen:
    if word not in dict_vowels:
        for letter in word:
            if letter in vowels:
                dict_vowels[word] += 1

sorted_by_vowels = sorted(dict_vowels.items(), key=itemgetter(1), reverse=True)
print(f'Most vowels is in the word "{sorted_by_vowels[0][0]}": {sorted_by_vowels[0][1]} vowels.')
