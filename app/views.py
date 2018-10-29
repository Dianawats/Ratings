from app.model import Users
from validate import validate_username, validate_password
import re


user = Users()


the_users = []

# def add_new_user(username, password, role):
    
#     new_user = Users(username, password, role)
#     the_users.append(new_user)
#     return True
    

def register():
    while True:
        print("Enter your username: ")
        username = input()
        if validate_username(username) == False:
            print("Username should be in characters")
            continue
        else:
            break
    print("-----------------------------")
    while True:
        print("Enter your password: ")
        password = input()
        if validate_password(password) == False:
            print("Password must have 7 characters with atleast a lowercase, uppercase letter and a number")
            continue
        else:
            break
    print("-----------------------------")
    # while True:
    print("Enter your role: ")
    role = input()
        # if validate_role(role) == False:
        #     print("Role should be characters")
        #     continue
        # else:
        #     break
    print("-----------------------------")

    username = username
    password = password
    role = role
    new_user = user.add_user(username, password, role)

    if len(the_users) > 0:
        print("New user added:")

        for user in the_users:
            print("")
            print( "Welcome "+ user.username )
            print("")

        return True
    return False 

    print(the_users)


def login(name, password):
    if any(user["name"] == name for user in the_users):
        if any(user["password"] == password for user in the_users):
            return True
        return False
