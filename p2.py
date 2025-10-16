#Write a program to print the square root of a number. Raise an exception if the number is negative.
import math
def sqrt(num):
    if num<0:
        raise ValueError("Cannot find square root for negative number.")
        print("Square root of", num, ":", math.sqrt(num))
    
try :
    n=int(input("Enter a number:"))
    sqrt(n)

except ValueError as e:
    print("Error:", e)
