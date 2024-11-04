import report_management
import jsonParser
import inventory_management
import main_menu
import datetime
import getpass

config = jsonParser("config.json")

with open(config["ppe"], 'r') as file:
    ppe_line = file.readlines()

# login purposes
def update_access_log(username, action):
    with open(config["access"], 'r') as file:
        line = file.readlines()
    if not (bool(line)):
        with open(config["access"], 'w') as file:
            file.write(f'{"Username":<8}   {"Action":<80}   {"Timestamp":>21}\n')
    time = datetime.datetime.today().strftime('%d %B %Y %H:%M:%S')
    with open(config["access"], 'a') as file:
        file.write(f'{username:<8}   {action:<80}   {time:>20}\n')

def login():
    attempt = 0
    while attempt < config["maximum_attempt"]: # ensure the log in function is run 3 attempts
        username = input('\nPlease enter your username: ')
        password = getpass.getpass('Please enter your password: ')
        lines = report_management.drag_record(config["controller"], True)
        # drag record from controller.txt, to check the validation of username and password
        for line in lines:
            name, key = line # lines return with [username  password], therefore need split to assigned it to variable
            if name == username and key == password: # if username matched and corresponding password matched
                print('\nAccess granted\nWelcome to the system, admin')
                update_access_log(username, 'Log in account')
                if not bool(ppe_line):
                    inventory_management.initialize(username)
                main_menu.menu(username)
                return True
        print('\nAccess denied\nPassword or username incorrect, please try again')
        attempt += 1
    return attempt # returning attempt = 3 to terminate the code
# function for the registration of controller account

def register():
    lines = report_management.drag_record(config["controller"], True)
    # drag record from controller.txt, to get the username and get the number of controller
    # indent:True means exclude the headline
    controller_username = []
    for line in lines:
        controller_username.append(line[0]) # to get the username of every controller
    admin = input('Please enter the admin password to run this action: ') # master password = 1234
    if admin == config["master_password"] and len(lines) == config["maximum_accounts"]:
        # if the user enter correct master passwrod but the number of controller reached maximum (4)
        print('The number of controller for this system is maxed out\nYou cannot perform register action')
        print('Please select another option')
        return False
    elif admin == config["master_password"] and len(lines) < (config["maximum_accounts"]):
        # user enter the correct master password, and there are slot left before reached maximum controller account
        while True:
            username = input('\nEnter a username: ')
            if username in controller_username:# to check whether username input has been taken or not
                print('Username has been taken\nPlease enter a new one')
            else:
                break
        password = input('Enter a password: ').strip() # take passowrd for the account, and strip any accidentally whitespace
        print('Account register successfully, can proceed to log in')
        update_access_log(username, 'Register an account')
        with open(config["controller"], 'a') as file: # insert a new controller record
            file.write(f'{username:<20}  {password:>20}\n')
        return True
    else: # if user provide the wrong admin password, return back to main body option menu
        print('\nInvalid admin password\nPlease select the option again')
        return False

def delete(username):
    alignment = []
    controller_lines = report_management.drag_record(config["controller"], False)
    print('\nBefore deleting the account, please enter the account password to verify yourself')
    verification = getpass.getpass('Password: ')
    for idx, line in enumerate(controller_lines):
        name, key = line
        if username == name and verification == key:
            print('Account deleted')
            controller_lines.pop(idx)
            update_access_log(username, 'Delete own account')
            for line in controller_lines:
                account_name, password = line
                alignment.append(f'{account_name:<20}   {password:>20}\n')
            with open(config["controller"], 'w') as file:
                for line in alignment:
                    file.write(line)
            return True
    print('Password enter incorrect, action cannot be be performed')
    return False