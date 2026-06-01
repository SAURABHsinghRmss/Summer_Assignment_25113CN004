print("Write a program to Generate Fibonacci series")
#------------------------------------------------------------------------------
def fibonacci(n):
    if (n == 0): return 0
    elif (n == 1): return 1
    else:
        a,b=0,1
        for j in range(2,n+1,1):
            c=a+b
            a,b=b,c
        return c


#------------------------------------------------------------------------------
def choice():
    ch=str(input("Do you want to continue (Y/N):"))
    if((ch=="N")or(ch=="n")or(ch=="Y")or(ch=="y")):
        return ch
    else:
        print("wrong input!")
        choice()
    
ch="y"
while((ch=="Y")or(ch=="y")):
    num=int(input("Enter a term to which series is to be printed ="))
    for i in range(0,num,1):
        print(fibonacci(i))
    print("===================================================================")
    ch=choice()
print("Exit done!")
