#count each letter - from high repetency to low

from collections import Counter

a=Counter("encyclopedia")
print(a)

print(a.most_common(3)) #first 3 in array format

print(a.clear())

print(a.most_common(3)) #return empty list; no error
