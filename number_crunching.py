'''
IP  5
     1 3 5 2 9
     7
OP 5 2
'''
size=int(input())
l=list(map(int,input().split()))
a=int(input())
for i in range(size):
    for j in range(i+1,size):
        if l[i]+l[j]==a:
            print(l[i],l[j])
        
