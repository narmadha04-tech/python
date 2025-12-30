#check if a number is Armstrong.. that is 153 = 1^3+5^3+3^3
n=input()
s=0
for i in n:
    m=len(n)
    s+=int(i)**m
if int(n)==s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
