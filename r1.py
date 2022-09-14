"""n = input("Enter Your Name")
d= n.split()
print(d)"""

#another method
"""a=input('Enter your Name\n').upper()
b=a.replace(" ","")
for j in b:
    print(j)"""

'''dic = {"Kondy":"Patna","Yukta":"Jamshedpur", "Naman":"Hubli", "Chirag":"Kharagpur","Kushal":"Gand"}
x= input("Enter the name whose birthplace you wanna know\n")
print(dic[x])'''

y,z,w= list(input('Enter 3 numbers separated by Space\n').split())
print(w)
if y>z and y>w:
    print(y,"Y ka Sabse Badaa!!")
elif z>y  and z>w:
    print(z,"Z ka Sabse Badaa!!")
elif w>y and w>z:
    print(w,"W ka Sabse Badaa!!")


    

