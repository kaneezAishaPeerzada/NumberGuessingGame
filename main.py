secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print(" Congratulations! You guessed the correct number.")
