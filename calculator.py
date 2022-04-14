num1 = input("please enter the first number: ")
num2 = input("please enter the second number: ")
operation = input("please enter the operation among +, -, *, /, **, %: ")

if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    result = float(num1) / float(num2)
elif operation == "**":
    result = float(num1) ** float(num2)
elif operation == "%":
    result = float(num1) % float(num2)

else:
    result = "the operation enter by the user is wrong "
print(result)

