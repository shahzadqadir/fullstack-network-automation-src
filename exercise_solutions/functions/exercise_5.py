# Problem Statement
#
# Write a function called password_validation it must take one parameter called password, 
# check if the password user supplied is at least 8 characters long, don't start with a number, 
# must have at least one number, and at least one special character. 
# If all these conditions are met return True, else return False

def check_special_character(password: str) -> bool:
    for ch in password:     # loop through password one character at a time
        if not ch.isalnum() and not ch.isspace():   # if current character is not a number/letter and also not a space
            return True                             # it means it is a special character, return True
    return False                                    # if no special character has been found by end of loop, just return False

def password_validation(password: str) -> bool:
    # check if password is less than 8 characters long
    # return False if conditiond not met, no need to go further
    if len(password) < 8:
        return False
    # check if first character is integer
    if password[0].isdigit():
        return False
    # check if password has a special character
    return check_special_character(password=password)
            
# to check for special character we have created another function
# we can call that function inside our main function and return whatever that function returns.
# it is neat and reusable. we can re-use check_special_character(password: str) if we need

result = password_validation('abc123')
print(result) # False
result = password_validation('1abcdefgh')
print(result)   # False
result = password_validation('1abcdefgh')
print(result)   # False
result = password_validation('abcdefgh1')
print(result)   # False
result = password_validation('abcdefgh1$')
print(result)   # True
result = password_validation('y1(5Y&40N')
print(result)   # True