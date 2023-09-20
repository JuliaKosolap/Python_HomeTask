# # Task1
#
# word = (input("Enter letters and/or digits: "))
# lettersNumber = 0
# digitsNumber = 0
# for i in range(len(word)):
#     if word[i].isalpha():
#         lettersNumber += 1
#     elif word[i].isdigit():
#         digitsNumber += 1
#     else:
#         print("Invalid value was provided")
#
# print(lettersNumber)
# print(digitsNumber)

# # Task2
# word = (input("Enter any word: "))
# symbol = (input("Enter any symbol that is present in this word: "))
# symbolsCount = 0
#
# for i in range(len(word)):
#     if word[i] == symbol:
#         symbolsCount += 1
#
# print(symbolsCount)

# # Task3
#
# initialPhrase = (input("Enter any phrase: "))
# wordToFind = (input("Enter word from phrase which you want to replace: "))
# wordToReplace = (input("Enter from you want to replace with: "))
#
# print(initialPhrase.replace(wordToFind, wordToReplace))

# Task4

sentence = "Hello. Nice to meet you."

print(sentence[2:3])
print(sentence[len(sentence) - 2])
print(sentence[0:5])
print(sentence[0: len(sentence) - 2])

newWord = ""
for i in range(0, len(sentence), 2):
    newWord = newWord + sentence[i]

print(newWord)

newWord = ""
for i in range(1, len(sentence), 2):
    newWord = newWord + sentence[i]

print(newWord)

print(sentence[::-1])

newWord = ""
reverted = sentence[::-1]
for i in range(0, len(reverted), 2):
    newWord = newWord + reverted[i]

print(newWord)

print(len(sentence))
