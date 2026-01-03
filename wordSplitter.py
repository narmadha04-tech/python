with open("example.txt", "r") as f:
    words = f.read().split()
    for word in words:
        print(word)