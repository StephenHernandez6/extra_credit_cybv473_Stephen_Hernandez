#Name: Stephen Hernandez
#Date: 11/17/25
#Assignment: Guessing Game extra credit


import random

play_again = "y"
all_attempts = []

while play_again.lower() == "y":

    number = random.randint(1, 100)
    guess = 0
    attempts = 0

    print("Guess a number between 1 and 100")

    while guess != number:
        try:
            guess = int(input("Enter a number: "))
            attempts += 1
        except ValueError:
            print("enter a number")
            continue

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Correct")
            print("You got it in {} attempts".format(attempts))
            all_attempts.append(attempts)

    play_again = input("Do you want to play again? (y/n): ")

    if len(all_attempts) > 0:
        avg = sum(all_attempts) / len(all_attempts)
        print("\n=== Statistics ===")
        print("Games Played: {len(all_attempts)}")
        print("Average attempts: {0:.2f}".format(avg))

    print("Thanks for playing!")