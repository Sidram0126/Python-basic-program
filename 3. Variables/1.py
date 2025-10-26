# 1 Swap two variables without using a third variable.
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

print("Before swaping")
print("a =", a)
print("b =", b)

# Swapping without using a third variable
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)

print("Before swaping")
print("c =", c)
print("d =", d)

# Swapping with another method without using the 3rd variable
c,d=d,c
print("After swapping:")
print("c =", c)
print("d =", d)