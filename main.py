import random

def main():
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    print(f"The random number is: {random_number}")

    # Prompt the user to guess the number
    guess = int(input("Guess the number: "))

    # Check if the guess is correct
    if guess == random_number:
        print("You guessed correctly!")
    else:
        print("Sorry, you guessed incorrectly.")

if __name__ == "__main__":
    main()