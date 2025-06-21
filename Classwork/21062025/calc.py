a=int(input("Enter No. 1:"))
b=int(input("Enter No. 2:"))
c=input("Enter your task:")

if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/':
    print(float(a/b))
elif c=='%':
    print(a%b)
elif c=='*':
    print(a*b)
else :
    print("Invalid Input")