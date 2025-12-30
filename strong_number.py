#check whether a number is strong number. 145 = 1 4 5 = 1!+4!+5!  =1+24+120 = 145
n = input()
total = 0

for digit in n:
    fact = 1
    for i in range(1, int(digit)+1):
        fact *= i
    total += fact

if total == int(n):
    print("Strong Number")
else:
    print("Not a strong number")
