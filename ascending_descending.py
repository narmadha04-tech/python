#ascending and descending without sort()

size=int(input())
l=list(map(int,input().split()))

for i in range(size):
    for j in range(size-1):
        if l[j]>l[j+1]:
            l[j], l[j+1]= l[j+1], l[j]
for i in l:
        print(i, end=" ")
print()       
for i in range(size-1, -1, -1):
      print(l[i], end=" ")
