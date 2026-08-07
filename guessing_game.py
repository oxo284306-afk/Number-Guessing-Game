import random

secret_number = random.randint(1, 10)
print("=== Number Guessing Game ===\n")
print("I'm thinking of a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print(f"❌ Wrong! The correct number was {secret_number}.")
    