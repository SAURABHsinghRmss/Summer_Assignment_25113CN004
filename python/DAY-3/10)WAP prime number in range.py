print("Write a program to Print prime numbers in a range")
#------------------------------------------------------------------------------
def rangeprimes():
    num=int(input("Enter a number ="))
    print("prime number in range of ",num)
    for i in range(2,num+1,1):
        t=1
        if(num%i == 0):
            print(i)

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
    rangeprimes()
    print("===================================================================")
    ch=choice()
print("Exit done!")
