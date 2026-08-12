import random


def choose_difficulty():
    while True:
        print("=== Number Guessing Game ===")
        print("""
        1. Easy
        2. Medium
        3. Hard
         """)
        choice = input("Choose difficulty: ")

        if choice == '1':
            max_number = 10
            max_attempts = 10
            return max_number, max_attempts
        elif choice == '2':
            max_number = 50
            max_attempts = 7
            return max_number, max_attempts
        elif choice == '3':
            max_number = 100
            max_attempts = 5
            return max_number, max_attempts
        else:
            print("Wrong choice! Please choose (1,2,3)")


def calculate_score(count_try, max_attempts):
    score = int(((max_attempts - count_try + 1) / max_attempts) * 100)
    return score


def play_game(max_number, max_attempts):
    right_number = random.randint(1, max_number)
    print(f"\nI'm thinking of a number between 1 and {max_number}")
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
                score = calculate_score(count_try, max_attempts)
                print(f"Congratulations! You guessed the number in {count_try} attempts.")
                print(f"Your score: {score}")
                break
            elif guess < right_number:
                print("Too Low! Try again.")
            else:
                print("Too High! Try again.")
                
            print(f"Attempts remaining: {max_attempts - count_try}")
        except ValueError:
            print("Please enter a valid number!")


def main():
    play_again = True
    while play_again:
        max_number,max_attempts = choose_difficulty()
        play_game(max_number,max_attempts)
        while True:
            answer = input("Play again? (y/n): ").lower()
            if answer not in ('y', 'n'):
                print("Wrong choice! Please choose (y or n).")
                continue
            elif answer == 'y':
                break
            else:
                print("Thanks for playing!")
                play_again = False 
                break


main()
