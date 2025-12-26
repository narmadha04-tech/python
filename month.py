n = int(input())
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if 1 <= n <= 12:
    print(months[n-1])
else:
    print("Invalid")
