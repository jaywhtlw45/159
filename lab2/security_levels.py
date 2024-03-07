# security_level.py
# author: Jason Whitlow

# To run program use command:
# python3 security_levels.py

# The program demonstrates the Bell-La-Paluda security model. This model follows 2 rules:
#       1. A process at a given security level may not read an object at a higher security level.
#       2. A process at a given security level may not write to an object at a lower security level.
# The program does not facilitate writing to a file, therefore only the first rule will be relevant.

# The program will contain 4 users. Each user has a different security level
# Security levels are 0(public), 1(limited), 2(secret), 3(top secret).

# The program generates 50 file numbers and stores them in file_permisions.txt. Note that the physical file is not created, therefore no reads/writes can occur on the files.
#       - file_permisions.txt contains the file name and security level of each file.

# Users are stored in shadow.txt 
#       - shadow.txt contains the username, password, and security level of each user.

import random
import sys

def create_user_file():
    users = [
            ('Alice', 'apass', 1),
            ( 'Bob',  'bpass', 2),
            ( 'Chase',  'cpass', 3),
            ( 'Dany',  'dpass', 4)
    ]
    with open('shadow.txt', 'w') as file:
        [file.write(f"{user}:{password}:{level}\n") for user, password, level in users]

def generate_file_permissions():
    file_array = [(f'file_{i}', random.randint(1,4)) for i in range(100, 150)]
    with open('file_permissions.txt', 'w') as file:
        [file.write(f"{file_name}:{permission}\n") for file_name, permission in file_array]

def get_user_data():
    with open('shadow.txt', 'r') as file:
        lines = file.readlines()
    return [line.strip().split(':') for line in lines]

# User chooses to login or 
def user_login():
    user_data = get_user_data()
    if len(user_data) < 1:
        sys.exit(1)

    while True:
        try:
            # User Selection
            print("\nSelect a user to login:")
            print("\t  User\t\tPassword\tSecurity Level")
            for index, (user, password, level) in enumerate(user_data, start=1):
                print(f"\t{index} {user}\t\t{password}\t\t{level}")
            print("\t0 EXIT PROGRAM")
                
            user_input = input("Enter selection 0-4: ")
            user_number = int(user_input)

            # Exit Program
            if user_number == 0:
                return 0, 0

            if user_number < 0 or user_number > len(user_data):
                raise ValueError("Invalid user selection!!!!!!!!!!!!\n")
            
            # Password Authentication
            user_input = input(f"Enter {user_data[user_number-1][0]}'s password: ")
            if user_input != user_data[user_number-1][1]:
                raise ValueError("Invalid password!!!!!!!!!!!!!!")
            
            return user_data[user_number-1][0], int(user_data[user_number-1][2])
        
        except ValueError as e:
            print(f"Error: {e}\n")

# Displays files the user has the ability to read
def display_readable_files(level):
    with open('file_permissions.txt', 'r') as file:
        lines = file.readlines()

    print('\nReadable Files')
    print('Filename\t Security Level')
    for line in lines:
        line = line.strip().split(':')
        file_level = int(line[1])

        if level >= file_level:
            print(f'{line[0]}\t\t{line[1]}')

# Displays files the user has the ability to write to
def display_writable_files(level):
    with open('file_permissions.txt', 'r') as file:
        lines = file.readlines()

    print('\nWritable Files')
    print('Filename\t Security Level')
    for line in lines:
        line = line.strip().split(':')
        file_level = int(line[1])

        if level <= file_level:
            print(f'{line[0]}\t\t{line[1]}')

# User selects from 3 options
def user_action(user, level):
    while True:
        print(f"\n{user}, you are Security Level {level}\nSelect an option:")
        print(f"\t1 Show READABLE files")
        print(f"\t2 Show WRITABLE files")
        print(f"\t3 LOGOUT")

        try:
            user_input = input("Choose an action: ")
            user_input = int(user_input)

            if user_input < 0 or user_input > 3:
                raise ValueError("Invalid user selection!!!!!!!!!!!!\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")

        if user_input == 1:
            display_readable_files(level)
        if user_input == 2:
            display_writable_files(level)
        if user_input == 3:
            break
        
def main():
    print("\nNOTE: This program follows the Bell-La_Paluda model")

    create_user_file()
    generate_file_permissions()

    # Run program
    while True:
        user, level = user_login()
        if user == 0:
            print('Exiting program....')
            break
        user_action(user, level)

main()