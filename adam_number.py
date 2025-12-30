#given number is Adam or Not. reverse(12) = 21; 12² = 144; reverse(144) = 441; 21² = 441
n = int(input())
temp = n
rev = 0
sq = temp * temp
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

rev_sq = 0
while sq > 0:
    rev_sq = rev_sq * 10 + (sq % 10)
    sq //= 10

if rev_sq == rev * rev:
    print("Adam Number")
else:
    print("Not a adam number")
