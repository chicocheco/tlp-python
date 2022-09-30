"""
print this pattern using only # and \n
   ##
  ####
 ######
########
########
 ######
  ####
   ##

computation of desired value:
row | desired value | empty spaces | difference
0       2               3               2
1       4               2               3
2       6               1               4
3       8               0               5
4       8               0               4
5       6               1               1
6       4               2               -2
7       2               3               -5

row | desired value | empty spaces | step doubled | absolute | absolute
4       2               3            4 * 2 = 8        8
3       4               2            3 * 2 = 6        6
2       6               1            2 * 2 = 4        4
1       8               0            1 * 2 = 2        2
0  skip this row
-1      8               0            -1 * 2 = -2      2
-2      6               1            -2 * 2 = -4      4
-3      4               2            -3 * 2 = -6      6
-4      2               3            -4 * 2 = -8      8
"""

for i in range(4, -5, -1):
    positive = abs(i)
    if positive == 0:
        continue
    step = positive * 2
    empty_spaces = positive - 1
    hashes = abs(step - 10)
    print(empty_spaces * ' ', hashes * '#')
