'''
5. Password Validator 
Create: 
validate_password(password) 
Password requirements: 
● Minimum 8 characters 
● At least one uppercase 
● At least one lowercase 
● At least one number 
● At least one special character 
Example: 
Password: Hello123 
Output: 
Invalid password: - Missing special character
'''

'''
Functional Approach
'''

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Minimum 8 characters required.")

    if not any(char.isupper() for char in password):
        errors.append("Missing uppercase letter.")

    if not any(char.islower() for char in password):
        errors.append("Missing lowercase letter.")

    if not any(char.isdigit() for char in password):
        errors.append("Missing number.")

    if not any(not char.isalnum() for char in password):
        errors.append("Missing special character.")

    if len(errors) == 0:
        print("Valid password.")
    else:
        print("Invalid password:")

        for error in errors:
            print("-", error)

    return errors


password = input("Password: ")
validate_password(password)
