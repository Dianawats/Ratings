from app.model import Users
from validate import validate_username, validate_password
import re


the_users = []


def add_new_user(username, password, role):
    
    new_user = Users(username, password, role)
    the_users.append(new_user)
    return True
    

def register():
    
    while True:
        print("Enter your username: ")
        username = input()
        if validate_username(username) == False:
            print("Please enter correct username...")
            continue
        else:
            break
    
    print("Enter your password: ")
    password = input()

    print("Enter your role: ")
    role = input()
        
    print("-----------------------------")
    print("-----------------------------") 

    username = username
    password = password
    role = role
    add_new_user(username, password, role)

    if len(the_users) > 0:
        print("")
        print("New user added:")
        print("-----------------------------")

        for user in the_users:
            print("")
            print( "Welcome "+ user.username )
            print("")

        return True
    return False   