name = 'Chris'
# first condition = false
# 2nd and 3rd no variable to compare, as long as not empty value , return TRUE
# empty list return false
if name == 'Tom' or 'Adam' or 'Alan':
    print('granted')
else:
    print('denied')

# Prove
# True
print(bool('hi'))
# name = 'Chris', False
print(bool(name == 'hi'))

shippingCharges = float(input('input your shipping charges: '))
if shippingCharges < 50:
    shippingCharges += 10
    print('Your shipping fee is ${0: .2f}'.format(shippingCharges))
elif shippingCharges >= 50:
    shippingCharges = 'Free'
    print(f'Your shipping fee is {shippingCharges}')

# initialize your variable every time to avoid confusion
GST = 0.05
HST = 0.13
PST = 0.06

country = input('what country are you in ? ').upper()
orderTotal = float(input('what is your order total ? '))
if country == 'CANADA':
    province = input('in which province ? ').upper()
    if province == 'ALBERTA':
        orderTotal += (orderTotal * GST)
    elif province == 'ONTARIO' or province == 'NEW BRUNSWICK' or province == 'NOVA SCOTIA':
        orderTotal += (orderTotal * HST)
    else:
        orderTotal += (orderTotal * PST) + (orderTotal * GST)
print('your total will be ${0:.2f} including taxes'.format(orderTotal))

# reversed string
string = 'python'
print(string[::-1])
print(''.join(reversed(string)))