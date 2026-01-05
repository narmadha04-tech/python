import json

data = {
    "Name" : "John Doe",
    "Training" : "Python with DS",
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

