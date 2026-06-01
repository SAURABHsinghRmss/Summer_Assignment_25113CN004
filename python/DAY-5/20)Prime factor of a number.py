print("Write a program to Find largest prime factor")
#------------------------------------------------------------------------------
def prime(n):
    for i in range(2,int(n/2)+1,1):
        if(n%i==0):
            return 1
    return 0

def primefactor(n):
    if(prime(n)==0):
        print(n," is the largest prime factor of ",n)
    else:
        z=(int(n/2))+1
        for i in range(1,z,1):
            if((n%i==0) and (prime(i)==0)):
                t=i
        if(t==1):
            print("No prime number exists for ",n)
        else:
            print(t," is the largest prime factor of ",n)


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
    if(num>1):
        primefactor(num)
    else:
        print("Enter number more than one!!")
        print("NO prime numbers exists for number less than or equal to 1 .")
    print("===================================================================")
    ch=choice()
print("Exit done!")
