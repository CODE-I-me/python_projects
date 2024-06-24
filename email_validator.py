import re

email=input("enetr an email: ")

email_pattern= r'^[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$' 

if re.match(email_pattern,email):
    print("eneterd email is valid")
    
else:
    print("eneterd email is not valid")