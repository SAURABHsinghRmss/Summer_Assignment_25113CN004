print("Write a program to Check whether a number is prime")
#------------------------------------------------------------------------------
def prime():
    num=int(input("Enter a number ="))
    t=1
    for i in range(1,int(num/2)+1,1):
        if(num%i == 0):
            t+=1
            break
    if(t==2):
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

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
    prime()
    ch=choice()
print("Exit done!")
