marks = int(input("Enter You Marks:"))

if marks<=100 and marks> 90 :
    print("A grade")
elif marks<=90 and marks>70 :
    print("B grade")
elif marks<=70 and marks>50 :
    print("C grade")
elif marks<=50 and marks>=36 :
    print("D grade")
elif marks<=35 and marks>=0 :
    print("F grade")
else :
    print("Invalid Input")