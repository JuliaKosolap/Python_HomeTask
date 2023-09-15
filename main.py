# #Task1.1
# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter one more number: "))
# number3 = int(input("Enter the last number: "))
#
# sum = number1 + number2 + number3
# prod = number1 * number2 * number3
#
# print(sum)
# print(prod)
#
# #Task1.2
# diagonal1 = int(input("Enter first diagonal length: "))
# diagonal2 = int(input("Enter second diagonal length: "))
#
# square = (diagonal1 * diagonal2)/2
# print(square)
#
# #Task1.3
# number = int(input("Enter 4-digit number: "))
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number // 10 % 10
# n4 = number % 10
#
# prod = n1 * n2 * n3 * n4
# print(prod)

# #Task2.1
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
#
# str1 = "max"
# str2 = "min"
# str3 = "average"
#
# if n1 < n2 < n3:
#     min = n1
# elif n2 < n1 < n3:
#     min = n2
# else:
#     min = n3
#
# if n1 > n2 < n3:
#     max = n1
# elif n2 > n1 < n3:
#     max = n2
# else:
#     max = n3
#
# average = (n1 + n2 + n3)/3
#
# action = (input("Enter one of the action: max, min or average: "))
#
# if action == "min":
#     print(min)
# elif action == "max":
#     print(max)
# elif action == "average":
#     print(average)
# else: print("Invalid value was provided")


# #Task2.2
# number = int(input("Enter number of meters: "))
# unit = (input("Enter a unit to which you want to convert your meters (miles, inches or yards): "))
#
# miles = number / 1609.344
# inches = number * 39.3701
# yards = number * 1.09361
#
# if unit == "miles":
#     print(miles)
# elif unit == "inches":
#     print(inches)
# elif unit == "yards":
#     print(yards)
# else: print ("Invalid value was provided")


# Task3.1
try:
    num = int(input("Enter number from 1 to 7: "))

    match num:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid number!")

except ValueError as e:
    print("Value should be only number from 1 to 7!")

# Task 3.2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 == num2:
        print("Numbers are the same")
    elif num1 < num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

except ValueError as e:
    print("Value should be a number only")


# Task3.3
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = (input("Enter math operation: "))

    match operation:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)
        case _:
            print("No such operation!")
except ValueError as e:
    print("Provided value was incorrect")

