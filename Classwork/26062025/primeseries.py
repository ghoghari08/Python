flag=0

for i in range (2,101):
    for j in range(2,101):
        if i%j==0:
            flag=1
            break
        if flag==0:
            print(f"Given Number {i} is Prime Number") 
        else:
            print(f"Given Number {i} is Not  Prime Number")  

            
            
           