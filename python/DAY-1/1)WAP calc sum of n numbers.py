print("Program to calculate sum of n natural numbers")
num=int(input("enter positive number :"))
a=num
sum=0
while(a>0):
    sum+=a
    a-=1

print("Sum of First",num,"natural numbers = ",sum)
