from TicTacToeBase import TicTacToe
from MiniTicTacToe import MiniTicTacToe
from Exceptions import NotAvailable
from numpy import where

class SuperTicTacToe(TicTacToe):
    """
    This class handles the Super Tic Tac Toe Game and should be instantiated once.
    \nWithin each cell of the Super Game, a Tic Tac Toe game is instantiated to be played.
    """
    def __init__(self) -> None:
        super().__init__()
        input("""
-_-_- INSTRUCTIONS -_-_-
              
You will find a board of Tic Tac Toe. Within each cell, 
a game of Tic Tac Toe must be played, and the winner of 
the game will mark the cell as own. Then, the winner can
decide where in the board to play the next game of Tic Tac Toe.
To win, the player must win three games of Tic Tac Toe in the 
Super Board. Press [Enter] to start.""")
    
    def showBoard(self):
        print("--- Super Tic Tac Toe Board ---")
        return super().showBoard()

    def askPlayerInputs(self, chooser: int) -> int:
        if chooser == 1:
            return super().computerMove()

        self.showBoard()
        print('Select an open cell to play the next game: ')
        while True:
            try:
                position = int(input(''))
                if not 0 <= position <= 8:
                    raise ValueError
                if position not in self.openSlots():
                    raise NotAvailable
            except ValueError:
                print('Please enter a number from 0 to 8.')
                continue
            except NotAvailable:
                print('Please select an open slot.')
                continue
            break
        return position

if __name__ == "__main__":
    # Initialize once the Super Tic Tac Toe Game
    game = SuperTicTacToe()
    miniGameWinner = 0
    
    while not game._gameOver:
        # Get game's position and play the Mini Game
        gamePosition = game.askPlayerInputs(miniGameWinner)
        miniGame = MiniTicTacToe(gamePosition)
        miniGame.startGame()
        miniGameWinner = miniGame._winner

        # Add the Mini Game's winner number and place it in the Super Tic Tac Toe Board
        game.addLetterToBoard(miniGameWinner, gamePosition)
        game.checkIfWinner(miniGameWinner)

        if miniGameWinner == 1:
            game.showBoard()



