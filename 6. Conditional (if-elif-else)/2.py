# 2 Grade a student based on marks: 90+ → A, 80–89 → B, 70–79 → C, below 70 → Fail.
marks = int(input("Enter the student's marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")
print("------------------------------")
