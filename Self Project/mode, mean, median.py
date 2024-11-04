from collections import Counter
import statistics


# mode
numlist = [1, 2, 3, 4, 5, 5, 4, 3, 5, 6, 3, 4, 5, 6, 8, 6, 5, 4]
temp = numlist.copy()
# print(list(set(numlist)))  # remove duplicate values, core is set(list)
Counter(numlist.sort()).keys()
# equal to list(set(list object)), I added sort method so that it is in order
# however the unique list cannot be print
print(Counter(numlist).values())
print(dict(Counter(numlist)))  # count the occurrence of unique element, ultimate alternative (no need previous code)
# print(statistics.mode(numlist))  # only give out one answer

max_occurrence = 0
answer = []
for number in temp:
    occurrence = temp.count(number)
    for number_occurrence in range(occurrence - 1):
        temp.remove(number)
    if occurrence > max_occurrence:
        max_occurrence = occurrence
        answer.clear()
        answer.append(str(number))
    elif occurrence == max_occurrence:
        answer.append(str(number))
answer.sort()
print(f"\nThe mode is {', '.join(answer)}")

my_list = {}
for number in numlist:
    if number in my_list:
        my_list[number] += 1
    else:
        my_list[number] = 1
mode = max(my_list, key=my_list.get)
print(f'The mode is {mode}')
# mean
mean = sum(numlist) / len(numlist)
print(f'\nThe mean is {mean}')

mean = statistics.mean(numlist)
print(f'The mean is {mean}')

# median
remainder = len(numlist) % 2
place = int(len(numlist) / 2)
if remainder == 0:
    median = (numlist[place] + numlist[place - 1]) / 2
    print(f'\nThe media is{median}')
else:
    median = numlist[int(place) - 1]
    print(f'\n{median}')

median = statistics.median(numlist)
print(f'The median is {median}')
