#Write a function to remove duplicates from a list (preserve order).

l=list(map(int,input().split()))
u=[]
for n in l:
    if n not in u:
        u.append(n)
print(u)
        
        
        
