#Write a program that prompts the user to enter two numbers and displays their sum. Raise an exception and handle it if a non-number value is given as inputdef add_numbers():
def add():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Sum of the two numbers:", num1 + num2)
    except ValueError:
        print("Error: Please enter valid numeric values.")

add()
