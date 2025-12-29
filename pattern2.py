'''
5
11111
00000
11111
00000
11111
'''

n=int(input())
for i in range(n):
    for j in range(n):
        if i%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
