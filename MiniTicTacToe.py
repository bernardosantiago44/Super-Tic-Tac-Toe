from TicTacToeBase import TicTacToe
from numpy import where

class MiniTicTacToe(TicTacToe):
    """
    This class handles the mini game played in each cell of the Super Tic Tac Toe.
    """
    def __init__(self, position: int) -> None:
        super().__init__()
        index = where(self._positions == position)
        self.__row = index[0][0]
        self.__column = index[1][0]

    def showBoard(self):
        print(f'--- Tic Tac Toe Row {self.__row}, Column {self.__column}  ---')
        return super().showBoard()

    def startGame(self) -> int:
        while not self._gameOver:
            self.askPlayerInput()
            self.checkIfWinner(0)
            self.computerMove()
            self.checkIfWinner(1)

if __name__ == "__main__":
    miniGame = MiniTicTacToe(2)
    miniGame.startGame()
    print(f'winner: {miniGame._winner}')