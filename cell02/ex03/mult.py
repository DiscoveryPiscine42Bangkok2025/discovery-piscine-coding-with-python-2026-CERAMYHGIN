#!/usr/bin/env python3
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Result = int(Num1*Num2)
print (Num1,"x",Num2,"=",Result)
if Result > 0:
    print ("The result is positive")
elif Result < 0:
    print ("The result is negative")
else:
    print ("The result is positive and negative")