'''
IP: 5          IP: 8
11011        11100111
11011        11100111
00000        11100111
11011        00000000
11011        00000000
                 11100111
                 11100111
                 11100111
'''

n=int(input())
r=n//2
for i in range(n):
    if n%2!=0:
        if i==r:
            print("0"*n)
        else:
            print("1"*r+"0"+"1"*r)
    else:
        if i==r-1 or i==r:
            print("0"*n)
        else:
            print("1"*(r-1)+"00"+"1"*(r-1))
   
