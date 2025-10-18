# 4 Take a number and print if it’s single-digit, double-digit, or triple-digit.
num = int(input("Enter a +ve number: "))
if 0 <= num < 10:
    print("The number is single-digit.")
elif 10 <= num < 100:
    print("The number is double-digit.")
elif 100 <= num < 1000:
    print("The number is triple-digit.")
else:
    print("The number is out of range.")
print("------------------------------")