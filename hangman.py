#hangman
import random

words = ["USA", "Australia", "Canada"]

choosen_word = random.choice(words)

# print(choosen_word)

masked_word = []

for x in choosen_word:
    masked_word.append("_")

print(masked_word)

lives = len(masked_word)

print(f"lives left :{lives}")

correct_characters = 0
while(lives >0 and correct_characters != len(choosen_word)):
    user_input = input("Choose character : \n")
    user_input = user_input.lower()
    found = False

    for i in range(len(choosen_word)):
        lower_chosen_word = choosen_word[i].lower()
        if user_input == lower_chosen_word and masked_word[i] == "_":
            print("Correct")
            correct_characters += 1
            masked_word[i] = choosen_word[i]
            found = True
            break

    if not found:
        lives -= 1
    
    print(f"lives left :{lives}")
    print("Word "+"".join(masked_word))
