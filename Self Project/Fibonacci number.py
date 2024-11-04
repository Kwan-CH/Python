import itertools

# [0, 1, 1, 2, 3, 5, 8, 13, 21, ...]


def fibonacci_sequence(lists, empty, occurrence):
    if len(lists) < occurrence:
        num = lists[-1] + lists[-2]
        lists.append(num)
        return True
    elif len(lists) == occurrence:
        print(f"\n{','.join(map(str, lists))}")
        lists.insert(0, 0)
        return True
    elif len(lists) > occurrence:
        for insert in range(2):
            num = lists[-1] + lists[-2]
            lists.append(num)
            empty.append(num)
        lists.clear()
        return False


sequence1 = [0, 1]
sequence2 = []
total = int(input("How many number do you want to include in the Fibonacci sequence: "))
frequency = int(input("How many numbers do you want to include in a row: "))
role = itertools.cycle([1, 2])
for i in range(int(total/frequency)):
    continue1 = True
    continue_ = True
    chances = next(role)
    if chances == 1:
        while continue1:
            continue1 = fibonacci_sequence(sequence1, sequence2, frequency)
    elif chances == 2:
        while continue_:
            continue_ = fibonacci_sequence(sequence2, sequence1, frequency)
