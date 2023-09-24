# Task1
import random
from math import ceil


def get_numbers_prod(numbers) -> int:
    result = 1
    for number in numbers:
        result = result * number
    return result


random_list = []
prod = 0
for i in range(0, 5):
    num = random.randint(1, 10)
    random_list.append(num)
print(random_list)

# Get production of numbers in a list
prod = get_numbers_prod(random_list)
print(prod)


def get_min_number(numbers):
    minimum_number = min(numbers)
    return minimum_number


# Get minimum number in a list
minimum = get_min_number(random_list)
print(minimum)


# Get count of prime numbers in a list
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(3, ceil(num ** 0.5) + 1, 2):  # this skips even numbers and only checks up to sqrt(x)
        if num % n == 0:
            return False
    return True


new_list = []
for number in random_list:
    prime = is_prime(number)
    if prime:
        new_list.append(number)
print(new_list)
count = len(new_list)
print(count)


# Remove a number from the list
def remove_number_from_list(num, list):
    new_list = []
    for element in random_list:
        if element == num:
            deleted = list.pop(random_list.index(element))
            new_list.append(deleted)
    return len(new_list)


random_list = [5, 3, 7, 10, 12, 4, 7]
number = 7
count = remove_number_from_list(number, random_list)
print(count)


def mix_lists(list1, list2):
    new_list = list1 + list2
    sorted(new_list)
    return new_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
mixed_lists = mix_lists(list1, list2)
print(mixed_lists)


# Get the power of numbers in the list
def raise_number_to_power(power, random_list):
    result_list = []
    for number in random_list:
        power_of_number = number ** power
        result_list.append(power_of_number)
    return result_list


power = 3
result = raise_number_to_power(power, random_list)
print(result)
