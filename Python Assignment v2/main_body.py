import user
import jsonParser
import report_management

config = jsonParser("config.json")

# drag infromation from controller.txt to stan by for checking whetehr got any admin registered or not (min 1)
controller = report_management.drag_record(config["controller"], True)

while True:
    print('\nWelcome to the Health Department PPE Inventory Management System')
    print('\nPlease select the option')
    choice = input('1) Register\n2) Log in\n3) Exit the system\nOption: ')
    if choice == '1':
        user.register() # user register account, after account successsful registered option menu display again for choice
    elif choice == '2':
        if len(controller) < 1: # if no admin, display option menu, and influence the user to register account
            print('There is no admin yet, please register an admin account')
        else:
            if user.login() == 3:
                print('You reached the number of attempts to log in')
                break
    elif choice == '3': # user exit system
        print('Thank you for using the system')
        break
    else:
        print('Please enter a valid input') # Error handling for input other than 1, 2, 3