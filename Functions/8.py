# 8 Function returning multiple values (sum and average of a list).
def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average
print("------------------------------")