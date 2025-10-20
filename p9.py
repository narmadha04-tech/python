#Write a Python program that asks the user to enter a word and tries to print the third letter of the word with except: handler.

def get_input():
    
    try:
        word=input("Enter a word:")
        letter=int(input("Enter the letter to be printed[in number]:"))
        ind=word[letter-1]
        print(f"The {letter} letter in {word} is:", ind)
        
    except:
        print("Something went wrong!! Check your credentials.")

get_input()
