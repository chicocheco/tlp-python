"""
const int ARRAY_SIZE = 10;
int intArray[ARRAY_SIZE] = {87, 28, 100, 78, 84, 98, 75, 70, 81, 68};

int start = 0;
int end = ARRAY_SIZE - 1;
for (int i = start + 1; i <= end; i++) {
    for (int j = i; j > start && intArray[j-1] > intArray[j]; j--) {
        int temp = intArray[j-1];
        intArray[j-1] = intArray[j];
        intArray[j] = temp;
    }
}

An insertion sort is not the most efficient sort for most circumstances,
and to tell the truth, the previous code is not even the most efficient way to
perform an insertion sort. It is reasonably efficient for small to moderately
sized arrays, however, and it is simple enough that it can be memorized.

It’s not enough to have access to someone else’s sorting code
that you don’t fully understand.
"""

lst = [87, 28, 100, 78, 84, 98, 75, 70, 81, 68]
print(lst)

start = 1  # start from second element
end = len(lst)
# INSERTION SORT ALGORITHM
for i in range(start, end):
    current = lst[i]
    j = i - 1
    # while index is in range (positive number) and previous element is greater than current,
    # swap the current value down one position in the array
    left = lst[j]
    while j >= 0 and left > current:
        lst[j + 1] = left
        j -= 1
    lst[j + 1] = current

print(lst)

# input [87, 28, 100, 78, 84, 98, 75, 70, 81, 68]
# output [28, 68, 70, 75, 78, 81, 84, 87, 98, 100]

"""
first round:
j = 0
element = 28
lst[0] = 87
lst[0] > element (87 > 28)? yes?
swaps 28 for 87 
lower j by 1
did we reach the end on the left? yes? 
if the order changed, set the last swapped value
if the order did not change, it does nothing visible (overwrite with the same value) 
"""