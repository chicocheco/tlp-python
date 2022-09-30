"""
print this pattern using only # and \n
#
##
###
####
###
##
#
"""

empty_spaces = 4
for i in range(3, -4, -1):
    hash_marks = empty_spaces - abs(i)
    print(f'{empty_spaces} - {abs(i)}', '#' * hash_marks)
