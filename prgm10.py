a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the thrid number"))
if(a>=b)and(b>=c):
    print(a,"is greater")
elif(b>=a)and(b>=c):
    print(b,"is greater")
else:
    print(c,"is geater")
