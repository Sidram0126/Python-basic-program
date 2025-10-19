# 5 List: Remove duplicates from a list.
numbers = [1, 2, 3, 1, 2, 1, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("List after removing duplicates:", unique_numbers)
print("------------------------------")