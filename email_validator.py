import re

email = input("Enter an email: ")
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Entered email is valid")
else:
    print("Entered email is not valid")
