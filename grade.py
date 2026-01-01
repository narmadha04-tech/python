#grade system

marks = []
for i in range(5):
    m = int(input("Enter mark: "))
    marks.append(m)
avg = sum(marks) / 5
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
else:
    grade = "Fail"
print("Average:", avg)
print("Grade:", grade)

