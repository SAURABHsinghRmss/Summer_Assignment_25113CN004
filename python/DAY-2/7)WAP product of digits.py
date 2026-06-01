print("Write a program to Find product of digits")
#------------------------------------------------------------------------------
def digitproduct():
    num=int(input("Enter a number ="))
    t=num
    p=1
    while(t!=0):
        p*=(t%10)
        t=int(t/10)
    print("Product of digit of ",num," = ",p)

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
    digitproduct()
    ch=choice()
print("Exit done!")
