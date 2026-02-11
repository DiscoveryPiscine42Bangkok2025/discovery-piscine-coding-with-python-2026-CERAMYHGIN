#!/usr/bin/env python3
old = [2, 8, 9, 48, 8, 22, -12, 2]
new = [num1 + 2 for num1 in old]
newest = [num2 for num2 in new if num2 >= 10]
print(old)
print(set(newest))