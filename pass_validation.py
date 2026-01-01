#password validation

password = input("Create password: ")
if len(password) >= 8 and any(c.isdigit() for c in password):
    print("Password accepted")
else:
    print("Password too weak")
