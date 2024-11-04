# updated version
import time

def Collatz_Conjecture(num):
    print('\nNumber: ', num)
    while num != 0:
        if num == 1:
            num = 0
        elif num % 2 == 1:  # remainder = 1, odd number
            num = 3 * num + 1
            print(num)
        elif num % 2 == 0:  # remainder = 0, even number
            num = int(num / 2)
            print(num)

# Start = particular number / initial value, End = end value, boolean (False for particular, True for loop)
def Calculation_mode(Start, End, boolean):  # None = null value
    if End is None and boolean:  # when need value type for condition, use isinstance()
        while True:  # execute with infinity option, while loop
            Collatz_Conjecture(Start)
            Start += 1
            time.sleep(3)
    elif End is not None and boolean:  # is / is not None for None (null value)
        for numbers in range(Start, End + 1):  # execute with user's desire range, for loop
            Collatz_Conjecture(numbers)
            time.sleep(3)
    else:  # perform Collatz Conjecture for a number only
        Collatz_Conjecture(Start)

try:
    choice = input('Do you want auto calculate or calculate a particular number?\n'
                       '1) particular\n'
                       '2) auto\n'
                       'Choice: ').lower()
    if choice == '1' or choice == 'particular':  # perform Collatz Conjecture for a particular number
        number = int(input('\nenter the number you want to perform Collatz Conjecture: '))
        Calculation_mode(number, None, False) # None = null value, no end value (None) and no repitition (False)
    elif choice == '2' or choice == 'auto':  # perform Collatz Conjecture for certain range or infinity
        mode = input('\nHow to end?\n'
                         '1) range\n'
                         '2) infinity\n'
                         'Choice: ').lower()
        if mode == '1' or mode == 'range':
            start = int(input('Please give the start up number: '))
            end = int(input('Please give the end number: '))
            Calculation_mode(start, end, True)
            # start at number given and end at number given, have repetition (True) == within a given range
        elif mode == '2' or mode == 'infinity':
            start = int(input('\nPlease give the start up number: '))
            Calculation_mode(start, None, True)
            # start at number given, does not end, have repetition (True) == infinity
except KeyboardInterrupt:
    print('You choose to exit the program\nClick Start to run again')
except ValueError:
    print('You enter the wrong type of value, please enter number')