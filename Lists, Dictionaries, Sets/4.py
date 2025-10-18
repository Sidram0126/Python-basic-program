# 4 List: Count how many times a value appears in a list.
numbers = [1, 2, 3, 1, 2, 1, 4, 5]
value_to_count = 1
count = 0
for num in numbers:
    if num == value_to_count:
        count += 1
print("Count of", value_to_count, "is:", count)
print("------------------------------")