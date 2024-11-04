cipher = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
message = input("type the message you want to encrypt/decrypt: ").upper()
cipherText = ''
key = int(input("key: "))
print("""choose the way
1) encryption
2) decryption""")
choice = int(input())
global position
if choice == 1:
    for character in message:
        if character == ' ':
            cipherText += ' '
        else:
            position = cipher.index(character) + key
            if position > 26:
                position -= 26
            cipherText += cipher[position]
elif choice == 2:
    for character in message:
        if character == ' ':
            cipherText += ' '
        else:
            position = cipher.index(character) - key
            if position < 0:
                position += 26
            cipherText += cipher[position]
print(cipherText)