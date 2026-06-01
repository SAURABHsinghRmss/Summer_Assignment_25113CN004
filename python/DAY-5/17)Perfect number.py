print("Write a program to Check perfect number")
#------------------------------------------------------------------------------
def perfect(n):
    sum=0
    for i in range(1,(int(n/2))+1,1):
        if(n%i==0):
            sum+=i
    if(sum==n):
        print(n," is a perfect number.")
    else:
        print(n," is not an perfect number.")

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
    num=int(input("Enter a number ="))
    if(num>0):
        perfect(num)
    else:
        print("Enter number more than zero!!")
    print("===================================================================")
    ch=choice()
print("Exit done!")
