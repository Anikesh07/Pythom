#11
empty dictinory
print("how many elements?", end='')
n=int(input())
for i in range(n):
    print('enter keys',end='')
    k=input()
    print("Enter the values", end='')
    v=int(input())
    x.update({k:v})
    print("the dictonary are",x)x={} #e