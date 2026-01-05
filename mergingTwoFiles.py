with open("sample.txt", "r") as f1, open("output.csv", "r") as f2:
    text = f1.read() + "\n" + f2.read()
with open("merged_output.txt", "w") as f:
    f.write(text)
