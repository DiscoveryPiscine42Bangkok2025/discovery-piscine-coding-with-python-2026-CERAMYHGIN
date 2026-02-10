#!/usr/bin/env python3
Num = int(input("Enter a number less than 25: "))
if Num < 25:
    while Num <= 25:
        print ("Inside the loop, my variable is",Num)
        Num += 1
else:
    print ("Error") 


