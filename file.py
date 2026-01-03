#basic file operations

f = open("sample.txt", "w")  # write mode

f.write("Hello Guys!\nPython is fun.")

f.close()


f = open("sample.txt", "r")  # read mode

content = f.read()  # reads whole file
print(content)

f.close()


with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
# no need to explicitly close the file when using 'with' statement 


with open("sample.txt", "a") as f:
    f.write("\nThis line is added at the end.")
