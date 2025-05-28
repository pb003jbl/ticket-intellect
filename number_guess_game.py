import random
import math

def number_guess_game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("Too low. Try again.")
            elif guess > number:
                print("Too high. Try again.")
            else:
                optimal = math.ceil(math.log2(100))
                complexity = attempts / optimal
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                print(f"Guess complexity: {complexity:.2f} (your attempts / optimal: {optimal})")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guess_game()



