from random import randint


def play_guessing_game(from_int: int, to_int: int, num_of_tries: int):
    used_tries = 0
    number_to_guess = randint(from_int, to_int)

    print(f'Guess a number between {from_int} and {to_int}. You have {num_of_tries} tries.')

    while used_tries < num_of_tries:
        used_tries += 1
        
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess > to_int:
            print('The number is too high.')
        elif guess < from_int:
            print('The number is too low.')
        elif guess < number_to_guess:
            print('Try a higher number.')
        elif guess > number_to_guess:
            print('Try a lower number.')
        else: # guess == numer_to_guess
            print('You guessed the number!')
            return
    
    print(f'You have used all your tries. The number was {number_to_guess}.')
    

play_guessing_game(1, 10, 3)