print("Write a program to Check whether a number is palindrome")
#------------------------------------------------------------------------------
def palindrome():
    num=int(input("Enter a number ="))
    t=num
    sum=0
    while(t!=0):
        sum=(sum*10)+(t%10)
        t=int(t/10)
    if(sum==num):
        print(num,"is palindrome.")
    else:
        print(num,"is not palindrome.")

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
    palindrome()
    ch=choice()
print("Exit done!")
