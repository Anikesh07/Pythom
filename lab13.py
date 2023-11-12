#wap to accept three intger and largest of the three integer
a=int(input("Enter the 1st number="))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if a>b>c:
    print("Largest number is =",a)
elif b>a>c:
    print("Largest number is=",b)
else:
    print("Largest number is=",c)