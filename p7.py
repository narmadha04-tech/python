#Write a python program that has multiple except blocks. 
#Write a Python program that takes two inputs from the user — a number and a filename and tries to divide 100 by the number and open the given file. Use multiple except blocks to handle these possible errors
def check():
    while True:
        try:
            num=int(input("Enter a number to be divided by 100:"))
            fname=input("Enter a file to be opened:")
            print(f"{num} divided by 100:", 100/num)
            print("File opened.", open(fname, 'r'))

        except ValueError:
            print("It is not a number.")

        except ZeroDivisionError:
            print("Cannot be divided.")

        except FileNotFoundError:
            print(f"No file named {fname}")

        except Exception as e:
            print("Some other error occured")
check()
