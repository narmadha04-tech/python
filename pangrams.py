n="The quick brown fox jumps over the lazy dog"
n=n.lower()
s=set(n.replace(" ", ""))

if len(s)==26:
    print("Is a Pangram")

else:
    print("Not a pangram")