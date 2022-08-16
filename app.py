"""Number Guessing Game"""
import random
from statistics import mean, median, mode

# Initialize variables
play_game = 'y'
number_range_low = 1
number_range_high = 100
high_score = 0
list_of_game_attempts = []
number_of_attempts_out_of_range = 0
number_of_attempts_nan = 0
number_of_attempts_too_low = 0
number_of_attempts_too_high = 0


while play_game.lower() == 'y':
    print('/' * 79)
    print('')
    print("Welcome to the Number Guessing Game - Now With Stats!".center(79))
    if high_score != 0:
        print(f'▶▶▶ HIGH SCORE: {str(high_score)} ◀◀◀'.center(79))
    print(' ')
    print('╭─────────────────── Instructions ────────────────────╮'.center(79))
    print("│      I'm thinking of a number between 1 and 100.    │".center(79))
    print("│   Try to guess it in as few attempts as possible.   │".center(79))
    print('╰─────────────────────────────────────────────────────╯'.center(79))
    print('')

    # Set per game variables
    number_to_guess = random.randint(number_range_low, number_range_high)
    number_of_guesses = 0
    guess = input(
        f"Guess a number between {number_range_low} and {number_range_high}: ")

    while guess != number_to_guess:
        # Attempt count includes out of range and nan guesses
        number_of_guesses += 1

        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid number.")
        else:
            if guess < number_range_low:
                print(
                    f"Number not in range. Try higher between {number_range_low} and {number_range_high}!")
            elif guess > number_range_high:
                print(
                    f"Number not in range. Try lower between {number_range_low} and {number_range_high}!")
            elif guess > number_to_guess:
                print("It's lower!")
            elif guess < number_to_guess:
                print("It's higher!")

        if guess != number_to_guess:
            guess = input("Guess again: ")
        elif guess == number_to_guess:
            list_of_game_attempts.append(number_of_guesses)
            print('')
            print("You got it!".center(75))

            if high_score == 0 or number_of_guesses < high_score:
                high_score = number_of_guesses
                print(
                    f"▶▶▶ You set a new high score! Just {number_of_guesses} to guess the number ◀◀◀".center(75))
            else:
                print(
                    f"It took you {number_of_guesses} tries to guess the number.".center(75))
                print(f"The high score is still: {high_score}.".center(75))

            print('')
            print('Game Play Analysis ---------------------------------------')
            print(f"  Number of games played: {len(list_of_game_attempts)}")
            print("  List of scores: ", list_of_game_attempts)
            print(
                f"  > Median score (sorted middle value): {median(list_of_game_attempts)}")
            print(
                f"  > Mode score (most occurring value): {mode(list_of_game_attempts)}")
            print(f"  > Mean score (average): {mean(list_of_game_attempts)}")
            print('----------------------------------------------------------')
            print('')

    play_game = input("Do you want to play again? (Y/N): ")

print('')
print('Thanks for playing!')
print('')
