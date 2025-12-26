#check whether the given date is valid or not
date=input()
d,m,y=date.split("/")
d=int(d)
m=int(m)
y=int(y)
if(d>0 and d<=31) and (m>0 and m<=12) and (y>=1900 and y<=9999):
    print("Valid")
else:
    print("Invalid")

