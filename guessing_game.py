import random

secret_number = random.randint(1, 10)
print("=== Number Guessing Game ===\n")
print("I'm thinking of a number between 1 and 10")

count_try = 0

while True:
    guess = int(input("Enter your guess: "))
    count_try += 1
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {count_try} attempts.")
        break
    elif guess < secret_number:
        print("Too Low! Try again.")
    else:
        print("Too High! Try again.")
