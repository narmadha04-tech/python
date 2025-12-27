s=input()
l=list(s)
for i in range(len(l)):
    if l[i] in "AEIOUaeiou":
        l[i]=' ' 
r=''.join(l)
print(r)
