from random import *
Answer = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
Words = choice(Answer)
print(Words)
words = Words.lower()
word = []
letters = []

for i in words:
    word.append(i)
    letters.append("_")

while True:
    for i in range(len(letters)):
        print(letters[i], end = ' ')
    print()

    letter = input("Enter : ")

    for i in range(0, len(word)):
        if letter == word[i]:
            letters[i] = letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")

    if letters == word:
        for i in range(len(letters)):
            print(letters[i], end = ' ')
        print()
        print("Success")
        break