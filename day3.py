#---------------------
#hangman
# import random

# words = ["USA", "Australia", "Canada"]

# choosen_word = random.choice(words)

# print(choosen_word)

# masked_word = []

# for x in choosen_word:
#     masked_word.append("_")

# print(masked_word)

# lives = len(masked_word)

# print(f"lives left :{lives}")

# correct_characters = 0
# while(lives >0 and correct_characters != len(choosen_word)):
#     user_input = input("Choose character : \n")
#     user_input = user_input.lower()
#     found = False

#     for i in range(len(choosen_word)):
#         lower_chosen_word = choosen_word[i].lower()
#         if user_input == lower_chosen_word and masked_word[i] == "_":
#             print("Correct")
#             correct_characters += 1
#             masked_word[i] = choosen_word[i]
#             found = True
#             break

#     if not found:
#         lives -= 1
    
#     print(f"lives left :{lives}")
#     print("Word "+"".join(masked_word))

# print("\n---------------------\n")
    
# if correct_characters == len(choosen_word):
#     print(f"You won with lives left :{lives}")
# else:
#     print("You lose")


# print("Word Status : "+"".join(masked_word))

#-----------------------------
#functions

# import functions
# from functions import greet_with_name, good_morning, good_bye, general_greet

# greet_with_name("Hitesh")

# good_morning("Monali")

# good_bye("Mahesh")

# general_greet(name = "Hitesh", greeting = "Good Morning")
# general_greet("Hitesh", "Good Morning")

def calculate_love_score(first, second):
    love_str = "LOVE"
    true_str = "TRUE"
    
    love_count = 0
    true_count = 0
    for x in love_str:
        love_count += first.count(x.lower())
        love_count += second.count(x.lower())
        
    for y in true_str:
        true_count += first.count(y.lower())
        true_count += second.count(y.lower())
        
    print(str(true_count)+str(love_count))
    
# calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
