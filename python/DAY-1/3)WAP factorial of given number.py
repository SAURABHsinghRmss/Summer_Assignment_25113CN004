print("Write a program to Find factorial of a number.")
num=int(input("Enter number :"))
a=num
f=1
while(a>0):
    f*=a
    a-=1
print("Factorial of",num,"=",f)
