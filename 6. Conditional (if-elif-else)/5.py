# 5 Simple calculator using if–elif–else (add, subtract, multiply, divide).
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input('''Choose an operation:
 1. addtion
 2.substraction 
 3.Multiplication
 4.Division 
 Enter the operation : ''')
if operation == "1":
    result = num1 + num2
    print("The result is:", result)
elif operation == "2":
    result = num1 - num2
    print("The result is:", result)
elif operation == "3":
    result = num1 * num2
    print("The result is:", result)
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
print("------------------------------")    