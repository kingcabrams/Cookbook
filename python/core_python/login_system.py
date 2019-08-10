"""System that allows the user to login or create a username and password"""
# Usage: python3 login_system register/login/delete/clear/users

import getpass
import shelve
import sys

s = shelve.open('login_storage.txt')

try:
    if sys.argv[1].lower() == 'register':
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        s[username] = password
    elif sys.argv[1].lower() == 'login':
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        if username in s:
            if s[username] == password:
                print("Welcome back " + username)
            else:
                print("Incorrect login information")
    elif sys.argv[1].lower() == 'delete':
        username = input("Enter the name of the user you would like to delete: ")
        password = getpass.getpass("Enter their password: ")
        if username in s:
            print("We are sorry to see you go " + username)
            del s[username]
        else:
            print("Deletion failed")
            print("Username not found")
    elif sys.argv[1].lower() == 'clear':
        s.clear()
        print('Database has been cleared')
    elif sys.argv[1].lower() == 'users':
        for name in s.keys():
            print(name)
    else:
        print('Invalid argument given')
except IndexError:
    print("No valid arguments found.")
    print("Read the usage of this program then try again.")

s.close()


