# Task 1

def degree_of_number(number, degree):
    if degree <= 1:
        return number

    return number * degree_of_number(number, degree - 1)


print(degree_of_number(5, 5))


# degree_of_number(5, 5) -> degree_of_number(5, 4) => 3125
# degree_of_number(5, 4) -> degree_of_number(5, 3) => 625
# degree_of_number(5, 3) -> degree_of_number(5, 2) => 125
# degree_of_number(5, 2) -> degree_of_number(5, 1) => 25
# degree_of_number(5, 1) => 1

# Task2

def print_stars(n):
    if n < 1:
        print("Invalid value")
        return
    elif n <= 1:
        return print("*")
    print("*", end="")
    return print_stars(n - 1)


n = 5
print_stars(n)


# print_stars(5) -> print_stars(4) => *
# print_stars(4) -> print_stars(3) => *
# print_stars(3) -> print_stars(2) => *
# print_stars(2) -> print_stars(1) => *
# print_stars(1) => *

# Task3

def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)


a = 2
b = 4
print(sum_range(a, b))

# a + sum_range(a + 1, b) -> a + sum_range(2, 4) => 2
# a + sum_range(a + 1, b) -> a + sum_range(3, 4) => 5
# a + sum_range(a + 1, b)) -> a + sum_range(4, 4) => 9
