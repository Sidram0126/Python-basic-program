# 3 Check if a person is eligible to vote and drive based on age.
age = int(input("Enter the person's age: "))
if age >= 18:
    print("The person is eligible to vote.")
    if age >= 16:
        print("The person is eligible to drive.")
    else:
        print("The person is not eligible to drive.")
else:
    print("The person is not eligible to vote.")
print("------------------------------")
