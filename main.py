#Task1
number1 = int(input("Enter a number: "))
number2 = int(input("Enter one more number: "))
number3 = int(input("Enter the last number: "))

sum = number1 + number2 + number3
prod = number1 * number2 * number3

print(sum)
print(prod)

#Task2
diagonal1 = int(input("Enter first diagonal length: "))
diagonal2 = int(input("Enter second diagonal length: "))

square = (diagonal1 * diagonal2)/2
print(square)

#Task3
number = int(input("Enter 4-digit number: "))
n1 = number // 1000
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10

prod = n1 * n2 * n3 * n4
print(prod)
