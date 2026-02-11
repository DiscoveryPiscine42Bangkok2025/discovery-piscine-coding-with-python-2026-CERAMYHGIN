#!/usr/bin/env python3
for Num1 in range(0,11):
    Num2 = 0
    result = ""
    while Num2 <= 10:
        result = result + " " + str(Num2 * Num1)
        Num2 += 1
    print("Table de",Num1,":",result)