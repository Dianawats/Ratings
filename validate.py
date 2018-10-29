import re

def validate_username(username):
    if not username:
        return False
    elif " " in username:
        return False
    elif not re.search(r"^[a-zA-Z]", username):
        return False
    else:
        return True
   

def validate_password(password):
    if not password:
        return False
    elif " " in password:
        return False
    elif not re.search(r"^(\d*(?=.*[a-zA-Z])[a-zA-Z\d]{5,7}$", password):
        return False
    else:
        return True