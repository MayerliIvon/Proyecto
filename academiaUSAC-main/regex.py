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

def isExplicityLetters(input_str):
    if re.fullmatch(r'[A-Za-z]+', input_str):
        return True
    else:
        return False

def isExplicityNumbers(input_str):
    if re.fullmatch(r'\d+', input_str):
        return True
    else:
        return False

def isExplicityValidEmailAddress(input_str):
    # This is a basic email pattern, might not cover all edge cases
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    if re.fullmatch(pattern, input_str):
        return True
    else:
        return False