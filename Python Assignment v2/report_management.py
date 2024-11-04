import jsonParser
import user

config = jsonParser("config.json")
item_dict = jsonParser("items.json")
lists_of_keys = list(item_dict.keys())
def drag_record(name, indent):
    with open(name, 'r') as file:   #drag record from name.txt file
        lines = file.readlines()
        item_list = []
        for line in lines:
            item_list.append(line.split())
        if indent:
            return item_list[1:] # exclude the title of each txt file
        else:
            return item_list

# add transaction line when receive/distribute
def transaction_update(supplier_hospital, item_code, quantity, date, initialize):
    with open(config["transaction"], 'a') as file:
        if initialize: # if initialized, add the headline
            file.write(f'{"From":<17}    {"To":<17}   {"Item_Code":<9}   {"Item_Name":<11}   {"Quantity(Box)":>13}   {"Date":>12}\n')
        if supplier_hospital.startswith('H'): # means distribute, Health_Department -> hospital
            file.write(f'{"Health_Department":<17}    {supplier_hospital:<17}   {item_code:<9}\
   {item_dict.get(item_code):<11}   {quantity:>13}   {date:>12}\n')
        else: # means receive, supplier -> Health Department
            file.write(f'{supplier_hospital:<17}    {"Health_Department":<17}   {item_code:<9}\
   {item_dict.get(item_code):<11}   {quantity:>13}   {date:>12}\n')

# display the option of different types of report can be generated
def report_type(username):
    while True:
        print('\nPlease select the option')
        choice = input('1) Available supplies\n2) Supplies that less than 25 boxes\n3) The distribution of a particular item\n4) List of supplies suppliers supplied\n5) List of hospitals with distribution items\n6) Transaction report for specific month\n7) Exit report section\nOption: ')
        if choice == '1':
            ascending()
            user.update_access_log(username, 'Generated all item in ascending order report')
        elif choice == '2':
            quantity_less_25()
            user.update_access_log(username, 'Generated item less than 25 box report')
        elif choice == '3':
            particular_distribution()
            user.update_access_log(username, 'Generated particular item distribution report')
        elif choice == '4':
            supplies_suppliers_supplied()
            user.update_access_log(username, 'Generated supplies supplier supplied report')
        elif choice == '5':
            hospital_supplies()
            user.update_access_log(username, 'Generated hospitals\' supplies report')
        elif choice == '6':
            transaction_month()
            user.update_access_log(username, 'Generated specific month transaction report')
        elif choice == '7':
            print('Returning back to main menu')
            break
        else:
            print('Invalid input, please try again')

# show the quantity of all ppe in ascending order
def ascending():
    ordered = []
    alignment = []
    lines = drag_record(config["ppe"], True)
    # purposely get record in a list of string, for the value assignation later
    for line in lines:
        supplier, item_code, item, quantity = line # split the string with whitespace and assigned to defined variable
        ordered.append([item_code, item, int(quantity)]) # take needed variable only
    ordered = sorted(ordered, key=lambda x:x[2]) # sort the ordered list in ascending order based on the quantity value
    with open(config["report"], 'w') as file: # write the result to the report.txt file
        file.write('The list of items that arrange in ascending order by quantity available\n\n')
        file.write(f'{"Item_Code":<9}   {"Item_Name":<12}   {"Quantity":>14}\n') # headline
        for item in ordered:
            alignment.append(f'{item[0]:<9}   {item[1]:<12}   {item[2]:>14}\n') # align the record
        for line in alignment:
            file.write(line)
        print('Report generated successfully, please refer to report.txt')
# show the ppe item that has less than 25 box of quantity
def quantity_less_25():
    items = []
    alignment = []
    lines = drag_record(config["ppe"], True)
    # purposely get record in list of string, easier for value assignation later
    # ['jcwiub', 'uwuvcwb'] like so
    for line in lines:
        supplier, item_code, item, quantity = line # split using whitespace and assigned to defined variable
        if int(quantity) < 25:
            items.append([item_code, item, quantity]) # if quantity less than 25, take the item_code, name and quantity
    with open(config["report"], 'w') as file: # write the result to the report.txt file
        file.write('The list of items that have less than 25 boxes of stock\n\n')
        file.write(f'{"Item_Code":<9}   {"Item_Name":<12}   {"Quantity":>14}\n') # headline
        for item in items:
            alignment.append(f'{item[0]:<9}   {item[1]:<12}   {item[2]:>14}\n') # align the record
        for line in alignment:
            file.write(line)
    print('Report generated succesfully, please refer to report.txt')

# show the prticular distribution of a ppe item, if it distribute to same hospital it will added up
def particular_distribution():
    title = ['From', 'To', 'Item_Code', 'Item_Name', 'Total']
    distribution = []
    alignment = []
    total = {} # store the quantity of items that distributed in each hospital
    transcation_lines = drag_record(config["transaction"], True)
    hospitals = drag_record(config["hospitals"], True)
    for line in transcation_lines:
        if line[0] == 'Health_Department':
            distribution.append(line) # just get the transaction where FROM is Halth Department, means distribution
    while True:
        chosen_item = input('\nEnter the item code you want to search: ').upper()
        if chosen_item in lists_of_keys: # chekc if the item code enter valid or not
            break
        else:
            print('Please enter a valid input')
    for line in distribution: # once valid, can start iterate through all transaction line that with chosen item code
        if line[2] == chosen_item:
            hospital_code = line[1]
            item = line[2]
            quantity = int(line[-2])
            key = (hospital_code, item)
            if key in total:
                total[key] += quantity # if the hospital has exist in the total, add up the value
            else:
                total[key] = quantity # hospital haven't exist in the total, set up a new element with the value
    for (hospital_code, item), quantity in total.items():
        for hospital in hospitals:
            if hospital_code == hospital[0]:
                alignment.append(f'{hospital[1]:<22}   {quantity:>14}\n') # search for the hopsital name based on hospital code
    with open(config["report"], 'w') as file: # write the output to the 'report.txt' file
        file.write(f'The list of {item_dict.get(chosen_item)} that had been distributed to\n\n')
        file.write(f'{"Hospital_Name":<22}   {"Quantity(Box)":>14}\n')
        for line in alignment:
            file.write(line)
    print('Report generated succesfully, please refer to report.txt')

# show the list of supplies supppliers supplied
def supplies_suppliers_supplied():
    supplier = drag_record(config["suppliers"], True)
    supplies = drag_record(config["ppe"], True)
    # both drag record return result in nested list [ [a, s, d, f], [s, w, e,r.d] ], like so
    items_supplied = {}
    alignment = []
    for company in supplier:
        temp = []
        for item in supplies: # loop through supplier.txt, if the supplier code is the same with the supplier code in ppe.txt
            if company[0] == item[0]: # this means this supplier supplied this supplies
                temp.append(item[2]) # add in the record
        items_supplied[company[-1]] = ', '.join(temp) # once end, join together
    alignment.append('The list of suppliers with their PPE equipments supplied\n\n')
    for company, supplies in items_supplied.items(): # group together the company and their supplies
        alignment.append(f'Suppliers: {company}\n')
        alignment.append(f'Supplies: {supplies}\n\n')
    with open(config["report"], 'w') as file: # write the output into the 'report.txt' file
        for line in alignment:
            file.write(line)
    print('Report generated succesfully, please refer to report.txt')
# show the list od ppe item that a hospital have
def hospital_supplies():
    hospitals = drag_record(config["hospitals"], True)
    transaction_line = drag_record(config["transaction"], True)
    # both drag record return result in nested list [ [a, s, d, f], [s, w, e,r.d] ], like so, exclude headline
    hospital_item = {}
    # a dictionary that store the items of each and every hospital have
    for hospital in hospitals:
        amount_per_item = {'HC': 0, 'FS': 0, 'MS': 0, 'GL': 0, 'GW': 0, 'SC': 0}
        # set initial value to 0 for all items, for individual hospital
        hospital_code = hospital[0] # take the hospital code, because the transaction line only have hospital code to match with
        for line in transaction_line:
            if hospital_code == line[1]:
                item_code = line[2]
                quantity = int(line[-2])
                if item_code in amount_per_item: # if the transaction line item_code is in the individual items list hospital
                    amount_per_item[item_code] += quantity # then add up together
        hospital_item[hospital[1]] = amount_per_item # after the transaction line end for a hospital, append the individual list to the main one (hospital_item)
        # and reset the individual for the next hospital
    with open(config["report"], 'w') as file: # write the output to the 'report.txt'
        file.write('The list of hospitals with the amount of items distributed\n')
        for hospitals, supplies in hospital_item.items():
            file.write(f'\n{hospitals}\n')
            for item_code, quantity in supplies.items():
                file.write(f'{item_code}: {quantity}\n')
    print('Report generated succesfully, please refer to report.txt')
# shows the transaction record (receive/distribute) for a specific month
def transaction_month():
    chosed_transaction = []
    transaction_line = drag_record(config["transaction"], True)
    # return record in nested list [ [a, d, e, r], [w, e,d s, f] ], and exclude headline
    while True:
        try:
            chosen_year = int(input('\nWhich year of the transaction you want to see: '))
            chosen_month = int(input('Which month of the year transaction you want to see (use number): '))
            for line in transaction_line: # loop through every transaction line
                day, month, year = line[-1].split('-')
                if int(month) == chosen_month and int(year) == chosen_year: # if the transaction line date is equal to the month and year input
                    chosed_transaction.append(line) # append the transaction line into the chosed_transaction
            with open(config["report"], 'w') as file: # write the output to 'report.txt' file
                file.write(f'This is the list of transaction that you want to see in month {chosen_month} in year {chosen_year}\n\n')
                file.write(f'{"From":<19}    {"To":<19}   {"Item_Code":<9}   {"Item_Name":<11}   {"Quantity(Box)":>14} {"Date":>15}\n')
                for line in chosed_transaction:
                    file.write(f'{line[0]:<19}   {line[1]:<19}   {line[2]:<9}   {line[3]:<11}   {line[4]:>14}   {line[-1]:>15}\n')
            break
        except ValueError: # error handling if the user input non-integer type value for month and year
            print('Please enter a valid input') # it will catch the error to prevent code terminate with error
    print('Report generated successfully, please refer to report.txt')