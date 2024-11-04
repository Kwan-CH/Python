import time
# bad naming variable


def calculation(z, w):
    b = first - 1
    print("\nNew Number :", first)
    time.sleep(1)
    while z >= 1:

        if z % 2 == 1:
            # the remainder is 1, means that is odd number
            z = 3 * z + 1
            print(z)

        elif z // 2 == 1:
            # final answer=1, means is the end of a number
            print("1\n")
            time.sleep(.5)
            if auto_particular == 1:
                z = 1
                b = b + 1
                z = z + b
                if w == 1:
                    time.sleep(.5)
                elif z > w:
                    return ()
                print("New Number :", z)
                time.sleep(1)
            else:
                z = 0

        elif z % 2 == 0:
            # the remainder is 0, means that is even number
            z = int(z / 2)
            print(z)


choice = "yes"
while choice == "yes":
    auto_particular = int(input("Auto calculate or calculate a particular number? (auto(1)/particular(2))\n"))
    if auto_particular == 1:
        first = int(input("Which number do you want to start first ? : "))
        print("How do you want to end? ")
        time.sleep(0.5)
        end = int(input("1)end within a range\n2)never\n1 or 2 ?\n"))
        if end == 2:
            end = 1
            j = calculation(first, end)
        elif end == 1:
            n_end = int(input("End at which number?"))
            j = calculation(first, n_end)

    if auto_particular == 2:
        print("How many numbers do you want to try ?")
        frequency = int(input())
        T = 1
        while T <= frequency:
            first = int(input("Which number? : "))
            j = calculation(first, 0)
            T = T + 1
    print(" Do you want to continue ? (yes/no)")
    choice = input(str())
print("Thanks for using ^-^ ")