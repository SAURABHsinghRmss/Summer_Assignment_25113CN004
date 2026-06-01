print("Write a program to Print factors of a number")
#------------------------------------------------------------------------------
def factors(n):
    z=(int(n/2))+1
    print("FACTORS ARE :")
    for i in range(1,z,1):
        if(n%i==0):
            print(i)
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
    num=int(input("Enter a number ="))
    if(num>0):
        factors(num)
    else:
        print("Enter number more than zero!!")
    print("===================================================================")
    ch=choice()
print("Exit done!")
