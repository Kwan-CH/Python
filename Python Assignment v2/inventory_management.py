import report_management
import jsonParser
import datetime
import user

config = jsonParser("config.json")
item_dict = jsonParser("items.json")
lists_of_keys = list(item_dict.keys())
# to get the list of item code, with the item_code only

lists_of_hospital = report_management.drag_record(config["hospitals"], True)
hospital_code = []
for hospitals in lists_of_hospital: # to get the list of code for each hospital
    hospital_code.append(hospitals[0])


# prompt user for the supplier code, item code and quantity
def information(action):
    while True:
        try:
            item_code = input('\nThe item code: ').upper()
            if item_code in lists_of_keys:   # to check the item code input exist or not
                quantity = int(input(f'The quantity {action}: '))
                if action.lower() == 'initialize':
                    code = input('The supplier code for the item: ').upper()
                elif action.lower() == 'receive': # if receive, the item code can act as foreign key to to take suppleir code
                    code = None # so no need to prompt for supplier code
                elif action.lower() == 'distribute':
                    while True:
                        code = input('The hospital code for the distribution: ').upper() # to check the hospital code input exist or not
                        if code in hospital_code:
                            break
                        else:
                            print('Please enter a valid input\n')
                currentDate = datetime.date.today()
                date = f'{currentDate.day}-{currentDate.month}-{currentDate.year}'
                # date = input()
                return code, item_code, quantity, date
            else:
                print('Please enter a valid input') # error handling if teh item code input does not exist
        except ValueError:
            print('Please enter a valid input') # error handling for unexpected data type input

def update_inventory(ppe):
    formatted = []
    for line in ppe:
        supplier_code, item_code, item_name, quantity = line   # line come with [supplier_code,item_code,item_name,quantity] a list of string, therefore need split
        alignment = f'{supplier_code:<13}   {item_code:<9}   {item_name:<13}   {quantity:>14}' # for alignment purposes
        formatted.append(alignment)
    with open(config["ppe"], 'w') as file: # update the ppe with the modification done
        file.write('\n'.join(formatted) + '\n')

# initialize the inventory / create inventory
def initialize(username):
    print('\nThe inventory seems like haven\'t initailize, please initialize the inventroy before proceeding to other functions')
    lines = [['Supplier_Code', 'Item_Code', 'Item_Name', 'Quantity(Box)']]
    for i in range(6):
        suppliers, item_code, quantity, date = information('initialize')
        # get necessary information
        lines.append([suppliers, item_code, item_dict.get(item_code), str(quantity)])
        report_management.transaction_update(suppliers, item_code, quantity, date, (True if i == 0 else False))
        # update transaction.txt
        # if i == 0 True for the writing of the headline of the file, when iterate again i = 1 no more headline to be write again
    update_inventory(lines) # update ppe.txt
    user.update_access_log(username, 'Initialized PPE inventory')

# check for item availability before distribute
def sufficiency(item, quantity):
    while True:
        try:
            if quantity > int(item[-1]): # if demand exceed supply, prompy user the enter their demand again
                # display available stock for reference
                print('\nThe item currently now is not sufficient to meet your demands')
                print('Please enter a appropriate value this time')
                print(f'The current availability of the item is {item[-1]}')
                quantity = int(input('The amount distribute: '))
            else:
                break
        except ValueError:
            print('Please enter a valid input')
    return quantity

# receive or distribute
def receive_distribute(username, ppe, action, plus_minus_one):
    # ppe comes with
    suppliers_hospital, item_code, quantity, date = information(action)
    # get necessary information when receive/distribute
    for item in ppe:
        if item_code in item:   
            if action == 'distribute': # means distribute, therefore need to check stock available before proceed to next
                # Health_Department -> hospital
                quantity = sufficiency(item, quantity)
            item[-1] = str(int(item[-1]) + (quantity * plus_minus_one))
            if suppliers_hospital is None: # means receive, search data in record dragged from 'ppe.txt', supplier -> Health Department
                for equipment in ppe: # and use item_code as foreign key to find the supplier code
                    if item_code in equipment:
                        suppliers_hospital = equipment[0]
            report_management.transaction_update(suppliers_hospital, item_code, quantity, date, False)
            user.update_access_log(username, f'{action.capitalize()} {quantity} {item_code} {"from" if action == "receive" else "to"} {suppliers_hospital}')
            # append the trasaction record
    update_inventory(ppe) # update the inventory (ppe.txt)
