lines=7
stars=1
spaces=lines-1
mid=lines//2
for i in range(lines):
    for k in range(spaces):
        print(" ",end="")
    for j in range(stars):
        if j==0 or j==stars-1:
            print("*",end="")
        else:
            print(" ",end="")    
    print()
    if i<mid:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1