#Write a program that raises an exception of class type.

class ShortNameError(Exception):
    pass

class Details:

    def get_input(self):
        while True:
            try:
                name=input("Enter your name:")
                if len(name)>2:
                    print("Verified!")
                    break
                else:
                    raise ShortNameError

            except ShortNameError:
                print("Name too short!!")
            
Details().get_input()
