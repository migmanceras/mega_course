#!/usr/bin/python3

"""
Project Description
This program creates a function that checks whether a username is valid based on some simple rules. The function will take a username as input and return whether it is valid or not. The rules for a valid username are:

The username must be between 5 and 15 characters.

It must contain only alphanumeric characters (letters and numbers).

It must start with a letter.

"""
min_len = 5
max_len = 15

def check_username_validity(username):
    if (len(username) <= max_len and len(username) >= min_len):
        print("Correct length")
        if(str.isalnum(username)):
            print("Only alpha-numeric characters")
            if (str.isalpha(username[0])):
                print("Starts with a letter")
    else:
        print("Username is not valid")


user_input = input("Insert username to check: ")
check_username_validity(user_input)