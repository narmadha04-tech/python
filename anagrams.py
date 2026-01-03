#anagrams

from collections import defaultdict

grp_an = defaultdict(list)
words = ["eat" , "tea" , "ate" , "nat" , "bat" , "cat"]

for word in words:
    key = ''.join(sorted(word))
    grp_an[key].append(word)
print(list(grp_an.values()))