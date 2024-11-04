def check(way):
    while way != 'identify' and way != 'range' and way.lower() != 'no':
        print('\nplease enter correct choice')
        way = input()
    return way


def prime_number(start):
    divisible_list = []
    if start in [2, 3, 5, 7]:
        list_.append(start)
    for prime_factor in [2, 3, 5, 7]:
        if start % prime_factor == 0:
            divisible_list.append(prime_factor)
    return divisible_list


list_ = []
print('''how do you want to find prime number?(identify/range)
identify: identify whether a specific number is a prime number or not 
range: identify how many prime numbers exist in a range of numbers and which is it''')
way = input()
checked_way = check(way)
while checked_way == 'identify' or checked_way == 'range':
    if checked_way == "identify":
        number = int(input("\nwhat number? "))
        if number == 1:
            print(number, "is not a prime number")
        else:
            z = prime_number(number)
            if not bool(list_):
                print(f"{number} is not a prime number because it can be divisible by {' and '.join(map(str, z))}")
            else:
                print(number, "is a prime number")
        print('''\ncontinue? if yes, (identify/range)
if no, type no''')
        way = input()
        checked_way = check(way)
    elif checked_way == "range":
        while checked_way == 'range':
            start = int(input("\nstart at what number? "))
            a = start
            end = int(input("end at what number? "))
            if start >= end:
                print("please enter correct number, initial value must greater than final value\n")
            else:
                list_.clear()
                for i in range(start, end + 1):
                    x = prime_number(i)
                print("\nthe list of prime numbers:")
                print(list_)
                print("there are", len(list_), "prime numbers in between", a, "and", end)
                print('\ncontinue? if yes, (identify/range) if no, type no')
                way = input()
                checked_way = check(way)
print("Thanks for using ^-^ ")
