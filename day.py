n = int(input())
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if n >= 0 and n <= 6:
    print(days[n])
else:
    print("Invalid")
