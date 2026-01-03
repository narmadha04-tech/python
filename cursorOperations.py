with open("sample.txt" , "r") as f:
    print(f.tell()) # Get the current cursor position
    print(f.seek(4)) # Move the cursor to position 10
    print(f.read()) # Read from the new cursor position