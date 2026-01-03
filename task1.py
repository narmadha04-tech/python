#task 1 - guven a list of colleges.  Use loop to pop the colleges not needed. 

colleges = ["IIT", "NIT", "Anna University", "KPR", "PSG"]

i = 0
while i < len(colleges):
    if colleges[i] != "KPR":
        colleges.pop(i)
    else:
        i+=1

print("College selected for admission:", colleges)

