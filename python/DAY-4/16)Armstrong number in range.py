print("Write a program to Print Armstrong numbers in a range")
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
        print(n)
        


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
    print("Armstrong number in range of ",num)
    for i in range(0,num,1):
        armstrong(i)
    print("===================================================================")
    ch=choice()
print("Exit done!")
