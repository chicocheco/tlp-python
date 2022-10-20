"""
In statistics, the mode of a set of values is the value that appears most often. Write
code that processes an array of survey data, where survey takers have responded to
a question with a number in the range 1–10, to determine the mode of the data set.
For our purpose, if multiple modes exist, any may be chosen.
"""

survey_data = [4, 7, 3, 8, 9, 7, 3, 9, 9, 3, 3, 10]
# to make the following algo relevant, you must group the values first
survey_data.sort()

most_freq = None
highest_freq = 0
current_freq = 0
for i in range(len(survey_data)):
    current_freq += 1
    # if (survey_data[i] IS LAST OCCURRENCE OF A VALUE)
    if i == len(survey_data) - 1 or survey_data[i] != survey_data[i + 1]:
        if current_freq > highest_freq:
            highest_freq, most_freq = current_freq, survey_data[i]
        current_freq = 0

print(f'Most frequent value is "{most_freq}" ({highest_freq}x)')

# or just use collections.Counter
