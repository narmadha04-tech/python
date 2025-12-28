#Split a list into two lists: even-index and odd-index elements.

l=list(map(int,input().split()))
even=[]
odd=[]
for i in range(len(l)):
    if i%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
print("Even index :", even)
print("Odd index :", odd)
