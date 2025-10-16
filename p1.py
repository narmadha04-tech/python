#Write a program that finds smaller of two given numbers. If the first number is smaller than the second, then generate an Assertion error.
num1=10
num2=35
if num2<num1:
    print("Smallest number is",num2)
else:
    assert num1<num2
    print("Assertion passed : First number must be greater.")
