import re

def check_email(email):
    pattern = r'^[a-zA-Z][\w]*@[a-zA-Z]+\.[a-zA-Z]{2,3}$'
    if re.match(pattern, email):
        return "The email you entered is valid."
    else:
        return "The email you entered is not valid."

print(check_email('george_tverdokhlib@gmail.com'))
