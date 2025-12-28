#count uppercase, lowercase, digits, and special characters in a string.
'''n=input()
uc=0
lc=0
d=0
s=0
for ch in n:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+=1
    elif ch.isdigit():
        d+=1
    else:
        s+=1
print(uc,lc,d,s)'''

#print uppercase, lowercase, digits, and special characters in a string.
n=input()
uc=[]
lc=[]
d=[]
s=[]
for ch in n:
    if ch.isupper():
        uc.append(ch)
    elif ch.islower():
        lc.append(ch)
    elif ch.isdigit():
       d.append(ch)
    else:
       s.append(ch)
print("Uppercase:",uc,)
print("Lowercase:",lc)
print("Digits:",d,)
print("Special:",s)
        
