import re

def validate_name(name):
    return bool(name and name.isalpha())

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def validate_phone_number(phone, contacts):
    if not phone.isdigit():
        return False
    for contact in contacts:
        if contact["phone"] == phone:
            return False
    return True
