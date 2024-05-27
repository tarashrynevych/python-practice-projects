import random
import sys

from dataclasses import dataclass, field

@dataclass
class RPS:
    moves: dict = field(default_factory=lambda: { 'rock': '🪨', 'paper': '📄', 'scissors': '✂️' })
    valid_moves: list[str] = field(init=False)
    winning_moves: dict = field(default_factory=lambda: { 'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper' })
    user_win_count: int = 0
    computer_win_count: int = 0
    tie_count: int = 0

    def __post_init__(self):
        self.valid_moves = list(self.moves.keys())
        
    def start_game(self):
            """Start the game.

            Prints a welcome message and starts the game loop.
            Allows the player to play the game until they choose to exit.
            """
            print('Welcome to Rock, Paper, Scissors!')
            print('Game started! Have fun')
            print('You can type "exit" to quit the game.')
            while True:
                self.play_game()
    
    def play_game(self):
        """
        Plays a round of the rock-paper-scissors game.

        This method prompts the user for their move, generates a random move for the computer,
        prints both moves, and checks the winner of the round.

        Parameters:
        None

        Returns:
        None
        """
        user_move = self.get_user_move()
        computer_move = random.choice(self.valid_moves)
        
        self.print_moves(user_move, computer_move)
        self.check_winner(user_move, computer_move)
        
    
    def get_user_move(self) -> str:
        """
        Prompts the user to enter their move and returns it.

        If the user enters 'exit', the program will exit and display the final game statistics.
        If the user enters an invalid move, they will be prompted to try again.

        Returns:
            str: The user's move.
        """
        while True:
            user_move = input('What is your move? ').lower()
            
            if user_move == 'exit':
                print('Thanks for playing!')
                print(f'You won {self.user_win_count} time(s), lost {self.computer_win_count} time(s), and tied {self.tie_count} time(s).')
                sys.exit()
                
            if user_move not in self.valid_moves:
                print('Invalid move. Please try again.')
                continue
            
            return user_move
        
    def print_moves(self, user_move: str, computer_move: str):
        """
        Prints the user's move and the computer's move.

        Parameters:
        - user_move (str): The move chosen by the user.
        - computer_move (str): The move chosen by the computer.

        Returns:
        None
        """
        print('---------')
        print(f'Your move: {self.moves[user_move]}')
        print(f'Computer\'s move: {self.moves[computer_move]}')
        print('---------')
        
    def check_winner(self, user_move: str, computer_move: str):
        """
        Determines the winner of a rock-paper-scissors game based on the user's move and the computer's move.

        Args:
            user_move (str): The move chosen by the user ('rock', 'paper', or 'scissors').
            computer_move (str): The move chosen by the computer ('rock', 'paper', or 'scissors').

        Returns:
            None

        Prints the result of the game: 'It's a tie!', 'You win!', or 'You lose!'.
        Updates the tie count, user win count, or computer win count accordingly.
        """
        if user_move == computer_move:
            self.tie_count += 1
            print('It\'s a tie!', end='\n\n')
        elif self.winning_moves[user_move] == computer_move:
            self.user_win_count += 1
            print('You win!', end='\n\n')
        else:
            self.computer_win_count += 1
            print('You lose!', end='\n\n')
            

rps = RPS()
rps.start_game()