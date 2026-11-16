# Jhulyana Timberlake
 # 11/01/2026
 # P1HW1
 # Calculating exponents and addition and subtraction

#Calculate exponents

print("----------Exponenets----------")
print()

base_number = int(input("Enter a base number: "))
exponent = int(input("Enter an exponment: "))
result = base_number ** exponent
print(base_number, "raised to the power of ", exponent, "is", result, "!!")

#calculate addition and subtraction
print()
print("----------Addition and Subtraction----------")
print()
num1 = int(input("Enter a staritng integer: "))
num2 = int(input("Enter a integer to add: "))
num3 = int(input("Enter a integer to subtract: "))

sum_result = num1 +num2
final_result = sum_result - num3
print(num1, "+", num2, "-", num3, "is equal to", final_result)