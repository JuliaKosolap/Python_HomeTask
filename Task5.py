# Task1
import numpy

numbers = [8, 3, -2, 10, 0, -4, 7, 3, -3, 10]
negative_sum = 0
for number in numbers:
    if number < 0:
        negative_sum = negative_sum + number
print(negative_sum)

double_numbers_sum = 0
for number in numbers:
    if numbers.count(number) > 1:
        double_numbers_sum = double_numbers_sum + number * 2
        numbers.pop(numbers.index(number))
print(double_numbers_sum)

unique_numbers = []
for number in numbers:
    if numbers.count(number) == 1:
        unique_numbers.append(number)
unique_numbers_sum = sum(unique_numbers)
print(unique_numbers_sum)

result_list = []
for i in range(1, len(numbers)):
    if i % 3 == 0:
        result_list.append(numbers[i])
print(numpy.prod(result_list))

print(max(numbers) * min(numbers))

numbers = [8, 3, -2, 10, 0, -4, 7, 3, -3, 10]
first_positive_index = 0
last_positive_index = 0
for i in range(len(numbers) - 1):
    if numbers[i] > 0:
        first_positive_index = i
        break

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = i
        break
new_list = numbers[first_positive_index + 1:last_positive_index]
print(sum(new_list))

# Task2
numbers = [3, 8, -2, 10, 0, -4, 7, 3, -3, 10]
repeated_numbers = []
for number in numbers:
    if numbers.count(number) > 1:
        repeated_numbers.append(number)

print(repeated_numbers)

unique_numbers = []
for number in numbers:
    if numbers.count(number) == 1:
        unique_numbers.append(number)

print(unique_numbers)

negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)

print(negative_numbers)

positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print(positive_numbers)