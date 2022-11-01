"""
In statistics, the mode of a set of values is the value that appears most often. Write
code that processes an array of survey data, where survey takers have responded to
a question with a number in the range 1–10, to determine the mode of the data set.
For our purpose, if multiple modes exist, any may be chosen.
"""

# what if the array is huge?
# refactored version of find-mode.py to speed it up, it is a “stock” version of “find the highest”

survey_data = [4, 7, 3, 8, 9, 7, 3, 9, 9, 3, 3, 10]  # values are in the range 1–10
# survey_data = [4, 7, 2, 8, 9, 7, 2, 9, 2, 2, 3, 10]  # values are in the range 1–10
print(survey_data)

# 1) initialize histogram with zeros (counters at 0)
histogram = [0] * len(survey_data)

# 2) place a value/counter at a corresponding index
# e.g. you counted 1s ("all ones") 3 times in the list, so histogram[0] returns 3
# (you can also leave index 0 with value 0 and add one element so that you could do histogram[0] = 3)
for i, v in enumerate(survey_data):
    histogram[v - 1] += 1
print(histogram)

most_frequent = 0
for i, v in enumerate(survey_data):
    if histogram[i] > histogram[most_frequent]:
        most_frequent = i

most_frequent += 1  # 0-indexing

print('The most frequent value and/or index: ', most_frequent)
