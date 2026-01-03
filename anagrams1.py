from collections import defaultdict

grp_an = defaultdict(list)

words = ["eat", "tea", "nat", "ate", "cat", "bat"]

for word in words:
    key = ''.join(sorted(word))
    grp_an[key].append(word)

print(list(grp_an.values()))

'''from collections import defaultdict

d = defaultdict(float)  # default value is 0
print(d["apple"], d["cat"]) 
d["apple"] += 1.5
print(d["apple"], d["cat"])'''
