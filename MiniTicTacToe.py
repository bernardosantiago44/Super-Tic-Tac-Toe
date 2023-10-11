from TicTacToeBase import TicTacToeBase
from numpy import where

class MiniTicTacToe(TicTacToeBase):
    def __init__(self, gamePosition):
        super().__init__()
        self.gamePosition = gamePosition
        index = where(self.boardPositions == gamePosition)
        self.__row = index[0][0]
        self.__column = index [1][0]

    def showBoard(self):
        print(f'                   Column {self.__column} Row {self.__row}')
        return super().showBoard()

if __name__ == "__main__":
    miniGame = MiniTicTacToe(7)
    miniGame.showBoard()
    miniGame.startGame()

