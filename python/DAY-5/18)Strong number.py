print("Write a program to Check strong number")
#------------------------------------------------------------------------------
def strong(n):
    t=n
    sum=0
    while(t!=0):
        p=1
        for i in range(1,(int(t%10)+1),1):
            p*=i
        sum+=p
        t=int(t/10)
    if(sum==n):
        print(n," is a strong number.")
    else:
        print(n," is not a strong number.")

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
        strong(num)
    else:
        print("Enter number more than zero!!")
    print("===================================================================")
    ch=choice()
print("Exit done!")
