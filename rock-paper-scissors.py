import random
import sys

from dataclasses import dataclass, field

@dataclass
class RPS:
    print('Welcome to Rock, Paper, Scissors!')
    moves: dict = field(default_factory=lambda: { 'rock': '🪨', 'paper': '📄', 'scissors': '✂️' })
    valid_moves: list[str] = field(init=False)
    winning_moves: dict = field(default_factory=lambda: { 'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper' })

    def __post_init__(self):
        self.valid_moves = list(self.moves.keys())
        
    def start_game(self):
        print('Game started! Have fun')
        print('You can type "exit" to quit the game.')
        while True:
            self.play_game()
    
    def play_game(self):
        user_move = self.get_user_move()
        computer_move = random.choice(self.valid_moves)
        
        self.print_moves(user_move, computer_move)
        self.check_winner(user_move, computer_move)
        
    
    def get_user_move(self):
        while True:
            user_move = input('What is your move? ').lower()
            
            if user_move == 'exit':
                print('Thanks for playing!')
                sys.exit()
                
            if user_move not in self.valid_moves:
                print('Invalid move. Please try again.')
                continue
            
            return user_move
        
    def print_moves(self, user_move: str, computer_move: str):
        print('---------')
        print(f'Your move: {self.moves[user_move]}')
        print(f'Computer\'s move: {self.moves[computer_move]}')
        print('---------')
        
    def check_winner(self, user_move: str, computer_move: str):
        if user_move == computer_move:
            print('It\'s a tie!', end='\n\n')
        elif self.winning_moves[user_move] == computer_move:
            print('You win!', end='\n\n')
        else:
            print('You lose!', end='\n\n')
            

rps = RPS()
rps.start_game()