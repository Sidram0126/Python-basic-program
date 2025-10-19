# 2. Check which number is greater using comparison operators.
# Using 2 numbers
num1=int(input("Enter your 1st number : "))
num2=int(input("Enter your 2nd number : "))
if num1>num2:
    print(f"{num1} is Greater number then {num2}")
else:
    print(f"{num2} is Greater number then {num1}")   
print("----------------------------------------------------")  

# Using 3 numbers
num1=int(input("Enter your 1st number : "))
num2=int(input("Enter your 2nd number : ")) 
num3=int(input("Enter your 3rd number : "))
if num1>num2 and num1>num3:
    print(f"The {num1} is Greater then {num2} and {num3}")
elif num2>num1 and num2>num3:
      print(f"The {num2} is Greater then {num1} and {num3}")  
else:
    print(f"The {num3} is Greater then {num1} and {num2}")  
print("----------------------------------------------------")  