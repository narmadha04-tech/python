#Write a program that prompts the user to enter his name. The program then greets the person with his name. But if the person's name is "Rahul" an exception is thrown and he is asked to quit the program.
def person():
    try:
        name=input("Enter your name:")
        if name == "Rahul":
            raise Exception("Error. Kindly exit the program, Rahul")
        print(f"Hello {name}. Welcome!!")
        
    except Exception as e:
        print(e)

person()
            
        

