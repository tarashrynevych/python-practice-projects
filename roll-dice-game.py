from random import randint

def roll_dice(amount: int) -> list[int]:
    """
    Rolls a specified amount of dice and returns the results.

    Parameters:
    amount (int): The number of dice to roll.

    Returns:
    list[int]: A list of integers representing the results of the dice rolls.
    """
    if amount <= 0:
        raise ValueError()
    
    return [randint(1, 6) for _ in range(amount)]

def play_game():
    while True:
        user_input = input('How many times you would like to roll the dice? ')
    
        if user_input.lower() == 'exit':
            print('Thanks for the game!')
            break
        
        try:
            roll_result = roll_dice(int(user_input))
            print(*roll_result, sep=', ')
            print('The sum of all numbers is', sum(roll_result))
        except ValueError:
            print('Please add a valid number')
            
play_game()