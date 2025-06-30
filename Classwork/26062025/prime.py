number=int(input("Enter A Number To check prime or not :"))
flag=0

for i in range(2,number):
    if number%i==0:
        flag=1
        break

if flag==0:
    print(f"Given Number {number} is Prime Number") 
else:
    print(f"Given Number {number} is Not  Prime Number")     