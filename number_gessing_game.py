import random
operator = random.randint(1, 100)
print("Welcome to number gessing game!")
user = ("guess a number between 1 and 100: ")
def number_guessing_game(): 
    while True:
        try:
            guess = int(input(user))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess < operator:
                print("Too low! Try again.")
            elif guess > operator:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the number!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
    print("Thank you for playing the number guessing game!")