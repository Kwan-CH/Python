import random
import time
# it is more satisfying to see in Thonny


message = input("Please enter your message : ")
word = ''
for letter in message:
    while True:
        character = chr(random.randint(32, 122))
        if character == letter:
            word += character
            print(word)
            time.sleep(0.01)
            break
        else:
            print(word + character)
            time.sleep(0.01)
