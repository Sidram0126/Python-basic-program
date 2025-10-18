# 10 Dict: Find the key with the highest value in a dictionary.
student = {"name": "Sid", "age": 26, "marks": 70, "grade": "A"}
max_key = max(student, key=student.get)
print("Key with highest value:", max_key)
print("------------------------------")