#Write a program that re-raises an exception.
#Write a Python program that asks the user to enter two numbers to divide and ses an inner and outer try-except to catch division by zero.
def div():
    while True:
        
        try:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = num1 / num2  
                print(f"Division of two numbers: {num1/num2}")
                
            except ZeroDivisionError:
                print("Either of the numbers is zero!!")
                raise
            
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                raise
            
            else:
                break
            
        except (ZeroDivisionError, ValueError):
            print("Error re-raised and handled. Try again.\n")

div()

