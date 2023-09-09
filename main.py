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

#Task2.1
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

str1 = "max"
str2 = "min"
str3 = "average"

if n1 < n2 < n3:
    min = n1
elif n2 < n1 < n3:
    min = n2
else:
    min = n3

if n1 > n2 < n3:
    max = n1
elif n2 > n1 < n3:
    max = n2
else:
    max = n3

average = (n1 + n2 + n3)/3

action = (input("Enter one of the action: max, min or average: "))

if action == "min":
    print(min)
elif action == "max":
    print(max)
elif action == "average":
    print(average)
else: print("Invalid value was provided")


