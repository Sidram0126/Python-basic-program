# 5 Change a variable’s value and track how its type changes (int → str → float).
# Initial integer value
var = 42
print(f"Value: {var}, Type: {type(var)}")

# Changing to string
var = str(var)
print(f"Value: {var}, Type: {type(var)}")

# Changing to float
var = float(var)
print(f"Value: {var}, Type: {type(var)}")