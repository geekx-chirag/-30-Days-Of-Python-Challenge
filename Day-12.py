import re

email = input("Enter your Gmail address: ")

if re.match(r".+@gmail\.com$", email):   # it will match either gmail ends with @gmail.com or not ?!
    print("Valid gmail address")
else:
    print("Not valid gmail address")
