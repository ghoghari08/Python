# for i in range(5):
#     for k in range(4-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# line=5
# star=1
# space=line-1
# for i in range(line):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(star):
#         print("*",end="")
#     print()
#     star+=1
#     space-=1

for i in range(5):
    print(" "*(4-i),"*"*(i+1))

