print("Write a program to Find LCM of two numbers")
#------------------------------------------------------------------------------
def lcm():
    num1=int(input("Enter 1st number ="))
    num2=int(input("Enter 2nd number ="))
    if(num1==0 and num2==0):
        print("LCM of ",num1," and ",num2," = zero")
    else:
        if(num1>num2):
            num=num1
        else:
            num=num2
        for i in range(1,num+1,1):
            if( (num1)%i==0 and (num2)%i==0 ):
                t=i
        print("LCM of ",num1," and ",num2," = ",((num1*num2)/t))


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
    lcm()
    print("===================================================================")
    ch=choice()
print("Exit done!")
