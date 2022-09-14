from datetime import date


f= input('Enter Your First Name\n')
l= input('Enter Your Last Name\n')
dob=date(int(input("Year:")), int(input("Month:")), int(input("Date:")))
addr = input('Enter your Address\n')
pinc = input('Enter your Pincode\n')
ct = input('Enter your City\n')
st = input('Enter Your State\n')
c_code = input('Enter Country_code\n')
ph_no= input('Enter Phone Number\n')
bg= input('Enter your Blood Group\n')
em= input('Enter your Email Address\n')
com = input('Enter your Company name\n')

#Age calc and string to date conversion
"""date_format = "%Y-%m-%d"  # %Y for year, %m for month and %d for day
dob_1 = datetime.datetime.strptime(dob, date_format)
todays_date = datetime.date.today()
age = int(dob_1.year() - todays_date.year())"""
today = date.today()
age = int((date.today() - dob).days/365)

print(f'Name: {f.capitalize()} {l.capitalize()}')
print(f'Age: {age}')
print(f'Address: {addr}, {pinc}, {ct}, {st} ')
print(f'Contact Number: {c_code}{ph_no} ')
print(f'Blood Group: {bg}')
print(f'Email: {em}')
print(f'Comapany Name: {com}')

