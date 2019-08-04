import random


def main():
    # Game setup
    print("Welcome to the guessing game")
    number_of_guesses = 7  # User has seven guesses before losing the game
    user_won = False

    # Computer guesses a random number between 1 and 10
    correct_answer = random.randint(1, 50)

    while number_of_guesses > 0:
        # Computer tells the user how many guesses they have left
        if number_of_guesses > 1:
            print("You have", number_of_guesses, "guesses left!")
        else:
            print("You have", number_of_guesses, "guess left")

        # User guesses the number
        user_guess = input("Guess my number: ")
        user_guess = int(user_guess)

        if user_guess == correct_answer:
            print("\nGood guess!")
            print("You are correct!")
            user_won = True
            break
        # Computer tells user whether guess was too high or too low
        elif user_guess > correct_answer:
            print("\nSorry, you guessed too high!")
        elif user_guess < correct_answer:
            print("\nSorry, you guessed too low!")

        number_of_guesses -= 1

    if user_won:
        print("You win!")
    else:
        print("You lose!")
        print("The correct number was", correct_answer, "!")


main()
