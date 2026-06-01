print("Write a program to Reverse a number")
#------------------------------------------------------------------------------
def reverse():
    num=int(input("Enter a number"))
    t=num
    rev=0
    while(t!=0):
        rev=(rev*10)+(t%10)
        t=int(t/10)
    print("Reverse of ",num," = ",rev)

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
    reverse()
    ch=choice()
print("Exit done!")
