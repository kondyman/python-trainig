#14th sept
from operator import truediv
import re

import re
while True:
    fname = input('Enter your First Name\n')
    y = re.search("[a-zA-Z]", fname)
    if y and len(fname)!=0 and fname.isalnum()!=True:
        print('\n')
        print("Proceed to fill the form further\n")
        break
    else:
        print('\n')
        print("Please enter a valid Name")

while True:
    lname = input('Enter your Last Name\n')
    j = re.search("[a-zA-Z]", lname)
    if j and lname.isalnum()!=True:
        print('\n')
        print("Proceed to fill the form further\n")
        break
    else:
        print('\n')
        print("Please enter a valid Name")

run=True
while run:
    num = input("Enter Your phone number\n")
    x = re.search("[0-9]", num)
    print(x)
    if x and len(num)==10:
        print('\n')
        print("Proceed to fill the form further\n")
        num = int(num)
        run=False
    else:
        print('\n')
        print("Please enter a valid Number")
        run=True


while True:
    age = input('Enter your Age\n')
    f = re.search("[0-9]", age)
    if f and 0<int(age)<999:
        print('\n')
        print("Proceed to fill the form further\n")
        age=int(age)
        break
    else:
        print('\n')
        print("Please enter a valid Age")

while True:
    city = input('Enter your City\n')
    g = re.search("[a-zA-Z]", city)
    if g and len(city)!=0:
        print('\n')
        print("Alright, Your form is submitted\nPlease have a look at your Details :")
        break
    else:
        print('\n')
        print("Please enter a valid City Name")

print(f'\nName: {fname.capitalize()} {lname.capitalize()}')
print(f'Age: {age}')
print(f'Contact Number: {num} ')
print(f'City: {city.capitalize()}')
