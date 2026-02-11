#!/usr/bin/env python3
Num1 = float(input("Give me a number: "))
result = round(Num1)
if result < Num1:
    print(result + 1)
elif result >= Num1:
    print(result)
