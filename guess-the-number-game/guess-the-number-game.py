import random

def play_game():
    secret_number = random.randint(0, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess the number between 0 and 100: "))
            if guess < 0 or guess > 100:
                print("Please enter a number between 0 and 100.")
                continue
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
            elif abs(guess - secret_number) <= 5:
                print("Very close!")
            elif guess < secret_number:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
        except ValueError:
            print("Please enter a valid number.")

play_game()