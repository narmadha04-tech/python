#cash withdrawal

balance = 10000
amount = int(input("Enter withdrawal amount: "))
if amount <= balance:
    balance -= amount
    print("Collect your cash")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")
