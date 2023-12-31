from TicTacToeBase import TicTacToeBase
from MiniTicTacToe import MiniTicTacToe

class SuperTicTacToe(TicTacToeBase):
    def __init__(self):
        self.nextGamePosition = -1
        self.lastPlayer = 1

        super().__init__()
        print('Instrucciones')
        self.showBoard()

    def showBoard(self):
        print('          --- Super Tic Tac Toe Board ---')
        return super().showBoard()
    
    def inputNextGamePosition(self):
        while True:
            try:
                self.nextGamePosition = int(input('Select an open cell to play the next game: '))
                if not 0 <= self.nextGamePosition <= 8:
                    raise ValueError 
                if not self.nextGamePosition in self.availableCells():
                    print('Please choose an open slot.')
                    continue
            except ValueError:
                print('Please enter a number from 0 to 8.')
                continue
            break
        print('\n\n')
    
    def startGame(self):
        while not self.gameOver:
            self.inputNextGamePosition()
            miniGame = MiniTicTacToe(self.nextGamePosition)
            miniGame.showBoard()
            miniGame.startGame()
            self.addMark(miniGame.winner, self.nextGamePosition)
    
superGame = SuperTicTacToe()
superGame.startGame()

