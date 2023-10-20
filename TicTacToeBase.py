import numpy as np
from Exceptions import NotAvailable

class TicTacToeBase:
    # Constructor class
    #    Takes no parameters.
    def __init__(self):
        # 0: o Mark
        # 1: x Mark
        # 2: Empty placeholder
        self.board = np.array([[2, 2, 2],
                               [2, 2, 2],
                               [2, 2, 2]
                          ])
        self.boardPositions = np.array([[0, 1, 2],
                                        [3, 4, 5],
                                        [6, 7, 8]
                              ])
        self.winner = -1
        self.lastPlayer = -1
        self.gameOver = False
    
    def showBoard(self):
        """Shows a 3x3 grid of the game's board."""
        baseBoard = """
                     {} | {} | {}
                    ---+---+---
                     {} | {} | {}
                    ---+---+---
                     {} | {} | {}
                    """
        # Internal mapping of the board
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
        """Returns a list with all the available cells for playing.
           Returns [] if no spaces are available."""
        # Get out existing board replacing 2's (empty cells)
        #  with True and any other value with False.
        # 
        open = (self.board == 2).flatten()
        available = []
        
        # Iterate through the array and keep only 
        # the positions of the empty cells.
        for i in range(0, len(open)):
            if open[i]:
                available.append(i)
        return available
    
    def addMark(self, player: int, position: int):
        """Add a player's mark to certain position in the board. \n
        ## Args:
            player (int): Player's number.
            position (int): Position in the board, previously validated [0, 8].
        """
        
        # Find the bidimentional index of the board
        # where the `position` lies.
        index = np.where(self.boardPositions == position)

        # Replace such index with the `player`'s mark.
        # Show the board and check if the player won.
        self.board[index] = player
        self.showBoard()
        self.checkForWinner(player)

    def inputPosition(self):
        if self.gameOver:
            return
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

    def endGame(self, player: int):
        self.winner = player
        self.gameOver = True

        if player == 0:
            print('Player o won')
        else:
            print('Player x won')

    def restartGame(self):
        self.winner = -1
        self.gameOver = False
        print('Draw. Please re-play game.')

        self.board = np.array([[2, 2, 2],
                               [2, 2, 2],
                               [2, 2, 2]
                          ])

    def checkForWinner(self, player: int):
        flatBoard = self.board.flatten()

        # horizontal or vertical win
        for i in range(len(self.board)):
            # Check if all 3 elements of a single row
            # are all True. This results in a winner being found.
            rows = all(self.board[i] == player)

            #columns 
            # Slice the flat board starting at i (0, 1, 2),
            # ending at the end with a step size of 3.
            columns = all(flatBoard[i::3] == player)
            if rows or columns:
                self.endGame(player)
                return
            
        # Slice the board array starting from zero (top leading corner) 
        # with a step of four (passing through the middle ending in bottom trailing)
        diagonal1 = all(flatBoard[0::4] == player)

        # Slice the board array starting from two (top trailing) with a step size
        # of two (passing throuhg four, the center, ending in bottom leading)
        diagonal2 = all(flatBoard[2:8:2] == player) 
        if diagonal1 or diagonal2:
            self.endGame(player)
            return
        if self.availableCells() == []:
            self.restartGame()
            self.showBoard()

    def startGame(self):
        while not self.gameOver:
            nextPosition = self.inputPosition()
            self.addMark(0, nextPosition)
            nextPosition = self.inputPosition()
            self.addMark(1, nextPosition)


if __name__ == "__main__":
    game = TicTacToeBase()
    game.showBoard()
    game.startGame() 