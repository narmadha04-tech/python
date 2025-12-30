#reverse number of the given number
n=int(input())
for i in range(len(str(n))):
    print(n%10, end="")
    n=n//10
