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

