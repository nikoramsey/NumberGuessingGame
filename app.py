import random

def guessing_game():
    print("!Welcome to the Number Guessing Game!")

    # Choose a difficulty level
    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    while True:
        try:
            difficulty = int(input("Enter 1, 2, or 3:"))
            if difficulty == 1:
                max_number, max_attempts = 50, 10
                break
            elif difficulty == 2:
                max_number, max_attempts = 100, 7
                break
            elif difficulty == 3:
                max_number, max_attempts = 200, 5
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    secret_number = random.randint(1, max_number)  # Generate a random number
    attempts = 0

    print(f"\nI have chosen a number between 1 and {max_number}. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            remaining_attempts = max_attempts - attempts

            if guess < secret_number:
                print(f"Too Low!! {remaining_attempts} attempts left.")

            elif guess > secret_number:
                print(f"Too High!! {remaining_attempts} attempts left.")
            else:
                print(f"CONGRATULATIONS!! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("ERROR! Invalid input! Please enter a number.")

    else:
        print(f"Game Over! The correct number was {secret_number}.")

# Run the Game
guessing_game()
