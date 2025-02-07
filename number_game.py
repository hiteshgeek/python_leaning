import random

choosen_number = random.randint(1,100)

attempts = 10
won = False

while attempts>0 and not won:
    attempts -=1
    guess = input("Guesss number [1-100]: ")
    guess = int(guess)

    if guess == choosen_number:
        print(f"You won. The numer is {choosen_number}. Left attempts {attempts}")
        won = True
    elif guess > choosen_number:
        print(f"Too high. Attempts left : {attempts}")
    else:
        print(f"Too low. Attempts left : {attempts}")

if not won:
    print("You lose")