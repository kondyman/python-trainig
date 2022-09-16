print('Radhe Radhe')
print(b'Alia Bhatt'.hex())
print('Ran\"beer\" Kapoor')

#storing output in a file
a=open('file.txt','w')
print('Crazy Duniya', file =a)
a.close()

#random choding
print('lilly'*3)

from datetime import date
todays_date = date.today()
print(todays_date.year)

n = input("Enter Your Name")
for i in range(len(n)+1):
    print(n[i])
