import json

with open('data.json', 'r') as f:
    content = json.load(f)
    print(content)
