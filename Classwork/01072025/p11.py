for i in range(1,6):
     for j in range(1,i+1):
         if(i==1 or i==2 ):
             print((i+j)-1,end=" ")
         elif(i==3):
             print((i+j),end=" ")
         elif(i==4):
             print((i+j)+2,end=" ")
         elif(i==5):
             print((i+j)+5,end=" ")
     print()