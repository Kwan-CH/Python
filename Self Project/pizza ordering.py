print("Welcome to pizza ordering system")
print("-----------------------------------\n")
# name and phone number
name = input("Please enter your name:")
phone = input("Please enter your phone number:")

# size of pizza
price = 0
while True:
    size = input("Please enter the size of the pizza you want (S-small/M-medium/L-large):").upper()
    if size == "S":
        price += 5
        size = "Small"
        break
    elif size == "M":
        price += 10
        size = "Medium"
        break
    elif size == "L":
        price += 15
        size = "Large"
        break
    else:
        print("\nPlease enter a valid input")

# type of pizza
while True:
    Type = input("Please enter the type of the pizza you want(M-Margherita/P-Pepperoni/H-Hawaiian):").upper()
    if Type == "M":
        price += 5
        Type = "Margherita"
        break
    elif Type == "P":
        price += 5
        Type = "Pepperoni"
        break
    elif Type == "H":
        price += 5
        Type = "Hawaiian"
        break
    else:
        print("\nPlease enter a valid input")

# toppings
while True:
    ingredient = ''
    topping = input("Please choose up to 3 toppings(m-mushroom/o-onion/p-pepper/e-extra cheese)").lower().split(", ")
    if len(topping) > 3:
        print("\nChoose only 3 toppings")
    else:
        for choice in topping:
            if choice.strip() == "m":
                price += 2.50
                ingredient += " Mushroom"
            elif choice.strip() == "o":
                price += 2.50
                ingredient += " Onion"
            elif choice.strip() == "p":
                price += 2.50
                ingredient += " Pepper"
            elif choice.strip() == "e":
                price += 2.50
                ingredient += " Extra cheese"
        break
print("\nYour pizza order is:")
print(f"{size}, {Type} with{ingredient}\n")
print("The total cost is RM", "%.2f" % price)
# print(f"The total cost is RM {price:.2f}")
print("Enjoy your pizza,", name)
