#program to accept the string and rotate the string n times
n=int(input())
s=input()
n=n%len(s)
r=s[n:]+s[:n]
print(r)
