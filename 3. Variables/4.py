# 4 Show the difference between global and local variables using a function.
# Global variable
x = "I am global"

def demonstrate_scope():
    # Local variable
    x = "I am local"
    print("Inside the function:", x)

# Calling the function
demonstrate_scope()

# Accessing the global variable
print("Outside the function:", x)
