# 4 Function to find the largest of three numbers.
def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print("------------------------------") 