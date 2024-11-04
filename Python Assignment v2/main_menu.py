import report_management
import inventory_management
import user
import jsonParser


config = jsonParser("config.json")

# update the hospital and supplier file when the update function is run
def update_supplier_hospitals_file(file_name, supplier_hospital_list):
    with open(file_name, 'w') as file:  # write the modification back to the selected txt file
        file.write(f'{f"{file_name[7:16].capitalize()}_Code":<15}   {f"{file_name[7:16].capitalize()}_Name":>25}\n')  # for alignment purposes, and select certain word only
        for line in supplier_hospital_list:
            file.write(f'{line[0]:<15}   {line[1]:>25}\n')  # for alignment purposes
    print(f'\nHere is the new list of the {file_name[7:16]} name:')
    for idx, name in enumerate(supplier_hospital_list):  # print the updated supplier/hospital list for better reference
        print(f'{idx + 1}) {name[-1]}')

def update_supplier(username): # update suppliers details, name
    supplier = report_management.drag_record(config["suppliers"], True)
    while True:
        print('\nHere is the list of the supplier name:') # print the list of supplier name
        for idx, company in enumerate(supplier):
            print(f'{idx + 1}) {company[-1]}')
        try:
            choice = int(input('Which supplier you want to change: '))
            if 0 < choice < len(supplier) + 1:
                print('\n*Please replace the whitespace in the name with underscore')
                new_supplier_name = input('What is the name of the new supplier: ')
                user.update_access_log(username, f'Change supplier name {supplier[choice - 1][-1]} to {new_supplier_name}')
                supplier[choice - 1][-1] = new_supplier_name
                update_supplier_hospitals_file(config['suppliers'], supplier)
                while True: # after a supplier name is changed, ask the continue want to continue to edit for the others
                    continue_modify = input('\nDo you want to continue updating suppliers (yes/no): ').lower() # prompt user to continue the update section or not
                    if continue_modify == 'no' or continue_modify == 'yes': # error handling for input other than 'yes' and 'no'
                        break
                    else:
                        print('Please enter a valid input')
                if continue_modify == 'no': # if the input is valid and 'no', therefore exit the function
                    break
            else:
                print('Please enter a valid input') # error handling for input outside the numeric range
        except ValueError:
            print('Please enter a valid input') # error handling for unexpected data type input

def update_hospital(username): # update suppliers details, name
    hospitals = report_management.drag_record(config["hospitals"], True)
    while True:
        print('\nHere is the list of the hospital name:')
        for idx, hospital in enumerate(hospitals): # print the list of hospital name
            print(f'{idx + 1}) {hospital[-1]}')
        try:
            choice = int(input('Which hospital you want to change: '))
            if 0 < choice < len(hospitals) + 1:
                print('\n*Please replace the whitespace in the name with underscore')
                new_hospital_name = input('What is the name of the new hospital: ')
                user.update_access_log(username, f'Change hospital name {hospitals[choice - 1][-1]} to {new_hospital_name}')
                hospitals[choice - 1][-1] = new_hospital_name
                update_supplier_hospitals_file(config["hospitals"], hospitals)
                while True:
                    continue_modify = input('\nDo you want to continue updating hospitals (yes/no): ').lower()  # prompt user to continue the update section or not
                    if continue_modify == 'no' or continue_modify == 'yes': # prevent user input other data except for yes/no
                        break
                    else:
                        print('Please enter a valid input')
                if continue_modify == 'no':
                    break
            else:
                print('Please enter a valid input') # error handling for the numeric range
        except ValueError:
            print('Please enter a valid input') # error handling for unexpected data type input
# same logic with the function above

def menu(username): # after successful log in, it will print the option of a controller can do
    while True:
        choice = input('\nPlease select the option:\n1) Received item\n2) Distribute item\n3) Update supplier details\n4) Update hospital details\n5) Generate report\n6) Delete account\n7) Log out\nOption: ')
        if choice == '1': # received supplies from supplier
            lines = report_management.drag_record(config["ppe"], False)
            inventory_management.receive_distribute(username, lines, 'receive', 1)
        elif choice == '2': # distribute supplies to hospitals
            lines = report_management.drag_record(config["ppe"], False)
            inventory_management.receive_distribute(username, lines, 'distribute', -1)
        elif choice == '3': # update supppliers details, name
            update_supplier(username)
        elif choice == '4': # update hospitals details, name
            update_hospital(username)
        elif choice == '5': # generate report, will go different function for more specific report type
            report_management.report_type(username)
        elif choice == '6':
            if user.delete(username):
                break
            else:
                print('Password enter invalid')
        elif choice == '7': # log out the controller account, and return back to main body option menu
            user.update_access_log(username, "Log out account")
            print('Logging out...')
            break
        else:
            print('Enter a valid input') # Error handling for input other than 1, 2, 3, 4, 5, 6