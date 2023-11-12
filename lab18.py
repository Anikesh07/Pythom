#wap to use various lis tprpcesing method 
num=[10,20,30,40,50]
n=len(num)
print("No. of element",n)
num.append(60)
print("After appending new lsit is",num)
num.insert(0,5)
print("num after inserting",num)
num1=num.copy()
print("after copying",num1)
num.extend(num1)
print("After extending",num)