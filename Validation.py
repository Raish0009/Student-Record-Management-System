def get_valid_number(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print("\nonly positive digits are available\n")

def get_valid_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print("\nOnly alphabets are allowed in name.\n")

def get_valid_contact(prompt):
    while True:
        contact = input(prompt)
        if contact.isdigit() and len(contact) == 10:
            return contact
        else:
            print("\nContact must be a 10-digit number.\n")