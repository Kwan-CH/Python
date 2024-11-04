# > = ascending , < = descending
lists = [12, 4, 2, 8, 10]
length = len(lists)

for i in range(length):
    for index in range(length - 1):
        if lists[index] > lists[index + 1]:
            lists.insert(index, lists[index + 1])
            lists.pop(index + 2)

print(lists)
