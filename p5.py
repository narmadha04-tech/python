#Write a program that validates user's input.
while True:
        try:
            name=input("Name:")
            age=int(input("Age:"))
            num=input("Mobile No:")
            email=input("Personal email:")
            if not name.isalpha():
               raise Exception("Error:Name is not a string.")
            if age<18 or age>100:
                raise Exception("Error:Invalid age.")
            if not num.isdigit() or len(num)!=10:
                raise Exception("Invalid mobile number.")
            if  '@' not in email or '.com' not in email:
                raise Exception("Invalid email address.")
            else:
                print("All inputs are valid.")
                break

        except Exception as e:
            print(e)

