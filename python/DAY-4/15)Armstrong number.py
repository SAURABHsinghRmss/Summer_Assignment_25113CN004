print("Write a program to Check Armstrong number")
#------------------------------------------------------------------------------
def digit(n):
    d=0
    while(n!=0):
        d+=1
        n=int(n/10)
    return d

def armstrong(n):
    d=digit(n)
    sum=0
    tn=n
    while(tn!=0):
        sum+=((tn%10)**(d))
        tn=int(tn/10)
    if(sum==n):
        print(n,"is an armstrong number.")
    else:
        print(n,"is not an armstrong number.")
        


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
    num=int(input("Enter a term to be printed ="))
    armstrong(num)
    print("===================================================================")
    ch=choice()
print("Exit done!")
