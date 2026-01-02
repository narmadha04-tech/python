#Operations in dictionary
dictEg = {
    'fruit' : 'apple',
    'seeds' : 'poisonous',
    'isItGoodForHealth' : 'Yes',
    'EatNApples' : 1
}
print(dictEg)
print()
dictEg['EatNApples'] = 5
print("Update value :", dictEg)
print()
dictEg['color'] = 'red'
print("Add a New Key–Value Pair :", dictEg)
print()
print("Access Value Using Key :", dictEg['fruit'])
print()
dictEg.update({
    'fruit': 'green apple',
    'vitamins': 'A, C'
})
print("New key-value pairs :", dictEg)
print()
print("Keys :", dictEg.keys())
print()
print("Values :", dictEg.items())
print()
print("Key-value pairs :", dictEg.items())
