# for UNICODE conversion ONLY, 8-digit of code
print("word --> binary code  (1)\nbinary code --> word  (2)")
message = input('Enter your message: ')
choice = int(input('Enter encrypt/decrypt method: '))
if choice == 1:
    encrypted = []
    for letter in message:
        # each word is converted into their corresponding unicode, then get converted into binary form
        binary = format(ord(letter), 'b')
        if len(binary) < 8:
            # to ensure each binary contains 8 digits
            for completion in range(8 - len(binary)):
                binary = '0' + binary
        encrypted.append(binary)
    message = ' '.join(encrypted)
    print(f"Your message is encrypted into {message}")

elif choice == 2:
    lists_of_binary = []
    for i in range(0, len(message), 8):
        lists_of_binary.append(message[i:i+8])
    word = []
    for code in lists_of_binary:
        unicode = code[::-1]
        total = []
        index = 0
        for number in unicode:
            # convert binary into decimal
            num = int(number)
            total.append((2 ** index) * num)
            index += 1
        word.append(chr(sum(total)))
    message = ''.join(word)
    print(f"Your message is decrypted into '{message}'")

''' prevent to get more confused 
morse_code = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.',
          'F': '.._.', 'G': '__.', 'H': '....', 'I': '..', 'J': '.___',
          'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___',
          'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_',        
          'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__',
          'Z': '__..', '0': '_____', '1': '.____', '2': '..___', '3': '...__',
          '4': '...._', '5': '.....', '6': '_....', '7': '..___', '8': '...__',
          '9': '____.', '.': '._._._', ',': '__..__', ' ': '/', '!': '_._.__'}
elif choice == 3:
    word = ''
    for letter in message:
        upper = letter.upper()
        character = morse_code.get(upper)   
        word += character + ' '
    message = word
    print(f"Your message is encrypted/decrypted into '{message}'")

elif choice == 4:
    word = []
    for morse in message.split():
        word.append(list(morse_code.keys())[list(morse_code.values()).index(morse)])
    message = ''.join(word)
    print(f"Your message is encrypted/decrypted into '{message}'")'''

