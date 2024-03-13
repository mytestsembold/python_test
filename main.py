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

    # Check if the random number is greater than 5
    if random_number > 5:
        print("The random number is greater than 5.")
    else:
        print("The random number is less than or equal to 5.")

    # Check if the random number is between 3 and 7
    if random_number >= 3 and random_number <= 7:
        print("The random number is between 3 and 7.")
    else:
        print("The random number is not between 3 and 7.")

    # Check if the random number is a multiple of 3
    if random_number % 3 == 0:
        print("The random number is a multiple of 3.")
    else:
        print("The random number is not a multiple of 3.")

    # Check if the random number is a multiple of 5
    if random_number % 5 == 0:
        print("The random number is a multiple of 5.")
    else:
        print("The random number is not a multiple of 5.")

    # Check if the random number is a multiple of 3 and 5
    if random_number % 15 == 0:
        print("The random number is a multiple of 3 and 5.")
    else:
        print("The random number is not a multiple of 3 and 5.")


if __name__ == "__main__":
    main()