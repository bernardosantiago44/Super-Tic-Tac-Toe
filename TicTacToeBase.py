import numpy as np
from Exceptions import NotAvailable

class TicTacToeBase:
    def __init__(self):
        # 0: o Mark
        # 1: x Mark
        # 2: Empty placeholder
        self.board = np.array([[1, 2, 1],
                               [1, 1, 2],
                               [1, 2, 2]
                          ])
        self.boardPositions = np.array([[0, 1, 2],
                                        [3, 4, 5],
                                        [6, 7, 8]
                              ])
        self.winner = -1
        self.lastPlayer = -1
        self.gameOver = False
    
    def showBoard(self):
        baseBoard = """
                     {} | {} | {}
                    ---+---+---
                     {} | {} | {}
                    ---+---+---
                     {} | {} | {}
                    """
        boardList = []
        internalBoard = self.board.flatten()
        for i in range(0, 9):
            if internalBoard[i] == 2:
                boardList.append(str(i))
            elif internalBoard[i] == 0:
                boardList.append('o')
            elif internalBoard[i] == 1:
                boardList.append('x')
        print(baseBoard.format(*boardList))
    
    def availableCells(self):
        open = (self.board == 2).flatten()
        available = []
        for i in range(0, len(open)):
            if open[i]:
                available.append(i)
        return available
    
    def addMark(self, player: int, position: int):
        index = np.where(self.boardPositions == position)
        self.board[index] = player

    def inputPosition(self):
        while True:
            try:
                position = int(input('Enter an available cell: '))
                if not 0 <= position <= 8:
                    raise ValueError
                if not position in self.availableCells():
                    raise NotAvailable
            except ValueError:
                print("Please enter a positive integer from 0 to 8")
                continue
            except NotAvailable:
                print("The cell you entered is not available.")
                continue
            break
        return position

    def endGame():
        pass

    def checkForWinner(self, player: int):
        # horizontal or vertical win
        for i in range(len(self.board)):
            #row
            rows = all(self.board[i] == player)

            #columns 
            columns = all(self.board.flatten()[i::3] == player)
            if rows or columns:
                self.endGame()
                return
        # Slice the board array starting from zero (top leading corner) 
        # with a step of four (passing through the middle ending in bottom trailing)
        diagonal1 = all(self.board.flatten()[0::4] == player)

        # Slice the board array starting from two (top trailing) with a step size
        # of two (passing throuhg four, the center, ending in bottom leading)
        diagonal2 = all(self.board.flatten()[2::2] == player) 
        if diagonal1 or diagonal2:
            self.endGame()
            return
        if self.availableCells() == []:
            # draw
            pass

game = TicTacToeBase()
# while not game.gameOver:
#     game.showBoard()
#     nextPosition = game.inputPosition()
#     game.addMark(0, nextPosition)
#     game.showBoard()
#     nextPosition = game.inputPosition()
#     game.addMark(1, nextPosition)
    
game.checkForWinner(1)
