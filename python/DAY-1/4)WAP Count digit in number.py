print("Write a program to Count digits in a number")
def count(num):
    c,a=0,num
    while(a>0):
        c+=1
        a//=10
    print("Number of digits in",num,"=",c)

def choice():
    ch=str(input("Do you want to continue (Y/N):"))
    if((ch=="N")or(ch=="n")or(ch=="Y")or(ch=="y")):
        return ch
    else:
        print("wrong input!")
        choice()
    
ch="y"
while((ch=="Y")or(ch=="y")):
    num=int(input("Enter a number :"))
    count(num)
    ch=choice()
        
