import random


while True:
    print("=== Number Guessing Game ===")
    choice = input("""
    1. Easy
    2. Medium
    3. Hard
    Choose difficulty: """)

    if choice == '1':
        max_attempts = 10
        max_number = 10
        right_number = random.randint(1, max_number)
        break
    elif choice == '2':
        max_attempts = 7
        max_number = 50
        right_number = random.randint(1, max_number)
        break
    elif choice == '3':
        max_attempts = 5
        max_number = 100
        right_number = random.randint(1, max_number)
        break
    else:
        print("Wrong choice! Please choose (1,2,3)")


print(f"\nI'm thinking of a number between 1 and {max_number}")

while True:
    count_try = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}")
                continue

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
                
            print(f"Attempts remaining: {max_attempts - count_try}")
        except ValueError:
            print("Please enter a valid number!")

    answer = input("Play again? (y/n): ").lower()
    if answer != 'y':
        break

