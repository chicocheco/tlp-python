"""
print this pattern using only # and \n
########
 ######
  ####
   ##

computation of desired value:

row | desired value | empty spaces | diff. from desired value
0       8 (2*4)               0                   8
1       6 (2*3)               1                   5
2       4 (2*2)               2                   2
3       2 (2*1)               3                   -1

row | empty spaces | desired value | desired value without * 2
0           0              8                   4
1           1              6                   3
2           2              4                   2
3           3              2                   1
"""

empty_spaces = 4
multiplication = 2
for i in range(4, 0, -1):
    left_indent = abs(i - empty_spaces)
    print(f'{left_indent * " "}{(i * "#") * 2}')
