"""
Print this pattern using only # and \n
#####
####
###
##
#
"""

# problem reduction: a square, but let's start simpler
# problem reduction: a line

# for i in range(5):
#     print('#', end='')

# problem reduction: a square

# for i in range(5):
#     for j in range(5):
#         print('#', end='')
#     print()  # add '\n'

# problem reduction: count down by counting up (page #28)
# (more like C++ problem but kept for clarity)
# display numbers 5 through 1 in Python is easy with reversed range()

# for i in range(5, 0, -1):
#     print(i)

# final solution

for j in range(5, 0, -1):
    print('#' * j)

# in C++:
"""
for (int row = 1; row <= 5; row++) {
    for (int hashNum = 1; hashNum <= 6 - row; hashNum++) {
        cout << "#";
    }
    cout << "\n";
}
"""