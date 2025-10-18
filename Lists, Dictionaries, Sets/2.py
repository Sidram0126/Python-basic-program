# 2 List: Find the maximum and minimum number in a list.
numbers = [34, 12, 5, 67, 23, 89, 1]
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("Maximum number:", max_num)
print("Minimum number:", min_num)
print("------------------------------")