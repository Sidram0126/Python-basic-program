# 3 List: Reverse a list without using reverse() function.
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print("Reversed list:", reversed_numbers)
print("------------------------------")