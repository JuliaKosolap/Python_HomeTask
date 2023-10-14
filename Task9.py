# Task 1
with open("Story1.txt", "r") as file1:
    result = file1.read()
    words = result.split(" ")
    new_result = []
    for word in words:
        if len(word) >= 7:
            new_result.append(word)

with open("Story2.txt", "w") as file2:
    for w in new_result:
        file2.write(w + " ")

# Task2
with open("Story1.txt", "r") as file1:
    result = file1.read()
    words = result.split(" ")
    print(len(words))
