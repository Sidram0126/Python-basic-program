# 1 Swap two variables without using a third variable.
a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))

# Swapping without using a third variable
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)