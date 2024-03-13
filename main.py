import random

def main():
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    print(f"The random number is: {random_number}")

    # Check if the random number is even
    if random_number % 2 == 0:
        print("The random number is even.")
    else:
        print("The random number is odd.")


if __name__ == "__main__":
    main()