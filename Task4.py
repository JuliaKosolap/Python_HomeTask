# # Task1
#
# word = (input("Enter letters and/or digits: "))
# letters_number = 0
# digits_number = 0
# for i in range(len(word)):
#     if word[i].isalpha():
#         letters_number += 1
#     elif word[i].isdigit():
#         digits_number += 1
#     else:
#         print("Invalid value was provided")
#
# print(lettersNumber)
# print(digitsNumber)

# # Task2
# word = (input("Enter any word: "))
# symbol = (input("Enter any symbol that is present in this word: "))
# symbols_count = 0
#
# for i in range(len(word)):
#     if word[i] == symbol:
#         symbolsCount += 1
#
# print(symbols_count)

# # Task3
#
# initial_phrase = (input("Enter any phrase: "))
# word_to_find = (input("Enter word from phrase which you want to replace: "))
# word_to_replace = (input("Enter from you want to replace with: "))
#
# print(initial_phrase.replace(word_to_find, word_to_replace))

# Task4

sentence = "Hello. Nice to meet you."

print(sentence[2:3])
print(sentence[len(sentence) - 2])
print(sentence[0:5])
print(sentence[0: len(sentence) - 2])

new_word = ""
for i in range(0, len(sentence), 2):
    new_word = new_word + sentence[i]

print(new_word)

new_word = ""
for i in range(1, len(sentence), 2):
    new_word = new_word + sentence[i]

print(new_word)

print(sentence[::-1])

new_word = ""
reverted = sentence[::-1]
for i in range(0, len(reverted), 2):
    new_word = new_word + reverted[i]

print(new_word)

print(len(sentence))
