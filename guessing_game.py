import random

right_number = random.randint(1, 10)
print("=== Number Guessing Game ===\n")
print("I'm thinking of a number between 1 and 10")

max_attempts = 5
count_try = 0

while True:
    guess = int(input("Enter your guess: "))
    count_try += 1
    if count_try == max_attempts and guess != right_number:
        print(f"Game Over!\nThe correct number was {right_number}.")
        break
    elif guess == right_number:
        print(f"Congratulations! You guessed the number in {count_try} attempts.")
        break
    elif guess < right_number:
        print("Too Low! Try again.")
    else:
        print("Too High! Try again.")
