print("Write a program to Find sum of digits of a number")
#----------------------------------------------------------------------------
def sumofdigit():
    num=int(input("Enter a number ="))
    t=num
    sum=0
    while(t!=0):
        sum+=(t%10)
        t=int(t/10)
    print("Sum of digits of ",num," = ",sum)

#----------------------------------------------------------------------------
def choice():
    ch=str(input("Do you want to continue (Y/N):"))
    if((ch=="N")or(ch=="n")or(ch=="Y")or(ch=="y")):
        return ch
    else:
        print("wrong input!")
        choice()
    
ch="y"
while((ch=="Y")or(ch=="y")):
    sumofdigit()
    ch=choice()
print("Exit done!")
        
