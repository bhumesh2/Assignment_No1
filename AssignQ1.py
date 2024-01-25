"""Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 
●       Implement a Python function called check_password_strength that takes a password string as input.
       * The function should check the password against the following criteria:
       * Minimum length: The password should be at least 8 characters long.
      * Contains both uppercase and lowercase letters.
      * Contains at least one digit (0-9).
      * Contains at least one special character (e.g., !, @, #, $, %).
●       The function should return a boolean value indicating whether the password meets the criteria.
●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
●       Provide appropriate feedback to the user based on the strength of the password. """
import re

def check_password_strength(pswd):
    len_err = len(pswd) < 8
    uppercase_err =  not re.search(r"[A-Z]",pswd)
    lowercase_err = not re.search(r"[a-z]",pswd)
    digit_err = not re.search(r"\d",pswd)
    specialchar_err = not re.search(r"\W",pswd)

    errors = []

    if len_err:
        errors.append("The password should be at least 8 characters long.")
    if uppercase_err:
        errors.append("The password contains uppercase letter.")
    if lowercase_err:
        errors.append("The password contains lowercase letter.")
    if digit_err:
        errors.append("The password contains at least one digit.")
    if specialchar_err:
        errors.append("The password contains at least one special character")

    if not errors:
        return "Password is strong."
    else:
        return "password is weak. please consider the following:\n" + "\n".join(errors)
    
pswd = input("enter the password :- ")
result = check_password_strength(pswd)
print(result)