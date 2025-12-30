#Count the number of occurrences of a digit in a given number
a, b = input().split()
count = 0
for i in a:
    if i == b:
        count += 1
print(count)
