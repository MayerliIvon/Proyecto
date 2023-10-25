import re

def CheckSecurity(password):
    if len(password) < 8:
        return 1
    elif not re.search(r'[A-Z]', password):
        return 2
    elif not re.search(r'[0-9]', password):
        return 3
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return 4
    else:
        return 5

