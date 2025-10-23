## Python builtin functions exercises

## 1)Multiply all numbers in a list.

from functools import reduce

nums = [2, 3, 4, 5]
result = reduce(lambda x, y: x * y, nums)
print(result)


## 2)Count upper and lower case letters.

s = input("Enter a string: ")
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


## 3)Check if a string is palindrome.

s = input("Enter a string: ")
if s.lower() == s[::-1].lower():
    print("Palindrome")
else:
    print("Not palindrome")


## 4)Invoke square root function after specific milliseconds.

import time, math

num = int(input())
ms = int(input())
time.sleep(ms / 1000)
print(f"Square root of {num} after {ms} miliseconds is {math.sqrt(num)}")


## 5)Return True if all elements of tuple are true.

t = (True, True, 1, "Hello")
print(all(t))
