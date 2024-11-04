# bad code
import random
import time
import itertools


def display_card(deck):
    suit_symbols = {'Hearts': '\u2661', 'Diamonds': '\u2662',
                    'Spades': '\u2664', 'Clubs': '\u2667'}
    tens = [10, 'J', 'K', 'Q']
    top = ''
    body = ''
    end = ''
    body_with_value = ''
    middle = ''
    before_end = ''
    for number in deck:
        top += "\t ________________"
        end += "\t|________________|"
        middle += f"\t|       {random.choice(list(suit_symbols.values()))}        |"
        if number == 10:
            number = random.choice(tens)
        if number == 10:
            body_with_value += f"\t| {number}             |"
            before_end += f"\t|             {number} |"
        else:
            body_with_value += f"\t| {number}              |"
            before_end += f"\t|              {number} |"
        body += "\t|                |"
    print(top)
    for frequency in range(11):
        if frequency == 1:
            print(body_with_value)
        elif frequency == 6:
            print(middle)
        else:
            print(body)
    print(before_end)
    print(end)


def player_role(choice):
    global value
    if choice == 'h':
        value = random.randint(1, 10)
        player_mark.append(value)
        print(f"\nPlayer value is {value}")
        print(f"Player's total value is {sum(player_mark)}")
    elif choice == 's':
        print(f"Player's total value is {sum(player_mark)}")


def dealer_role():
    global value
    if i == 3:
        value = random.randint(1, 10)
        dealer_mark.append(value)
        print(f'\nmysterious   #{value}')
        print(f"Dealer's total mark is {sum(dealer_mark)}")
    elif sum(dealer_mark) < 17:
        value = random.randint(1, 10)
        dealer_mark.append(value)
        print(f"\nDealer's value is {value}")
        print(f"Dealer's total mark is {sum(dealer_mark)}")


player = itertools.cycle([1, 2])
player_mark = []
dealer_mark = []
choice = 'h'
first_round = True
following_round = True
while following_round:
    while first_round:
        for i in range(4):
            player_turns = next(player)
            if player_turns == 1:
                player_role(choice)
                display_card(player_mark)
                time.sleep(2)

            else:
                dealer_role()
                display_card(dealer_mark)
                time.sleep(2)
        i = 0
        break
    first_round = False
    choice = input("h or s")
    if choice == 'h':
        player_role(choice)
        display_card(player_mark)
    elif choice == 's':
        player_role(choice)
        display_card(dealer_mark)
        if sum(player_mark) < sum(dealer_mark):
            print("dealer win")
            quit()
        else:
            while sum(dealer_mark) < 17:
                dealer_role()
                display_card(dealer_mark)
            print(f"Dealer's total mark is {sum(dealer_mark)}")
            following_round = False

if sum(player_mark) > sum(dealer_mark):
    print("player win")
else:
    print("dealer win")
