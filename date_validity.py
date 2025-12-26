time = input()
h, m, s = time.split(":")
h = int(h)
m = int(m)
s = int(s)
if (h >= 0 and h <= 23) and (m >= 0 and m <= 59) and (s >= 0 and s <= 59):
    print("Valid")
else:
    print("Not Valid")
