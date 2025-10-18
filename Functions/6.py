# 6 Recursive function to find factorial or Fibonacci sequence.
def recursive_function(n, type="factorial"):
    if type == "factorial":
        if n == 0:
            return 1
        else:
            return n * recursive_function(n-1, type)
    elif type == "fibonacci":
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return recursive_function(n-1, type) + recursive_function(n-2, type)
print("------------------------------")