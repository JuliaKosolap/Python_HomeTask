import random


def generate_random_list(list_len, start_value=1, end_value=100):
    return [random.randint(start_value, end_value) for _ in range(list_len)]


def binary_search(numbers_list):
    if len(numbers_list) == 1:
        answer = input(f"Is this number {numbers_list[0]}? Yes/No: ")
        if answer == "Yes":
            return numbers_list[0]
        else:
            return -1
    if len(numbers_list) == 2:
        answer = input(f"Is this number {numbers_list[0]}? Yes/No: ")
        if answer == "Yes":
            return numbers_list[0]
        else:
            answer = input(f"Is this number {numbers_list[1]}? Yes/No: ")
            if answer == "Yes":
                return numbers_list[1]
            else:
                return -1

    middle_index = len(numbers_list) // 2
    answer = input(f"Is this number {numbers_list[middle_index]}? Yes/No: ")

    if answer == "Yes":
        return numbers_list[middle_index]
    elif answer == "No":
        if len(numbers_list) > 2:
            range_question = f"Is this number from {numbers_list[0]} to {numbers_list[middle_index - 1]}? Yes/No: "
            if input(range_question) == "Yes":
                return binary_search(numbers_list[:middle_index])
            else:
                range_question = f"Is this number from {numbers_list[middle_index + 1]} to {numbers_list[-1]}? Yes/No: "
                if input(range_question) == "Yes":
                    return binary_search(numbers_list[middle_index + 1:])
                else:
                    return -1
        else:
            return binary_search(numbers_list[:middle_index])

    return -1


def create_list(start, end):
    numbers: list[int] = []
    for i in range(start, end + 1):
        numbers.append(i)
    return numbers


start_number = int(input("Hi. Now I will try to guess your number. Please enter start number for the list: "))
end_number = int(input("Now enter any end number for the list and after that think of any"
                       " number that is in the range of start number and end number: "))
nums = create_list(start_number, end_number)
print(nums)
result = binary_search(nums)
if result != -1:
    print(f"Your number is: {result}")
else:
    print("Your number was not found")
