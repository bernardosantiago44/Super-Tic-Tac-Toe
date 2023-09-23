from numpy import where, array, fliplr, random
from Exceptions import NotAvailable 

class TicTacToe:
    """
    Base Tic Tac Toe game properties.
    This class should not be instantiated. 
    """
    def __init__(self) -> None:

        # 0's represent o
        # 1's represent x
        # 3's represent an open slot
        self.__board = array([[3, 3, 3],
                              [3, 3, 3],
                              [3, 3, 3]])
        self._positions = array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])
        self._gameOver = False
        self._winner = -1
        
    def showBoard(self):
        boardList = []
        internalBoard = self.__board.flatten()
        BaseBoard = """
        {} | {} | {}
       ---+---+---
        {} | {} | {}
       ---+---+---
        {} | {} | {}
        """

        for i in range(0, 9):
            # 0's represent o
            # 1's represent x
            # 3's represent an open slot
            if internalBoard[i] == 0:
                boardList.append('o')
            elif internalBoard[i] == 1:
                boardList.append('x')
            elif internalBoard[i] == 3:
                boardList.append(f'{i}')

        print(BaseBoard.format(*boardList))

    def openSlots(self):
        openSlots = (self.__board == 3).flatten()
        availableNumbers = []
        for i in range(0, len(openSlots)):
            if openSlots[i]:
                availableNumbers.append(i)
        return availableNumbers
    
    def addLetterToBoard(self, letter: int, pos: int):
        index = where(self._positions == pos)
        self.__board[index] = letter

    def askPlayerInput(self):
        self.showBoard()
        while True:
            try:
                position = int(input("Select an open slot: "))
                if not 0 <= position <= 8:
                    raise ValueError
                if position not in self.openSlots():
                    raise NotAvailable
            except ValueError:
                print("Please enter a number from 0 to 8.")
                continue
            except NotAvailable:
                print("Please select an open slot.")
                continue
            break
        self.addLetterToBoard(0, position)

    def computerMove(self) -> int:
        available = self.openSlots()
        if len(available) != 0 and not self._gameOver:
            position = random.choice(available)
            self.addLetterToBoard(1, position)
            return position
        

    def checkIfWinner(self, playerNum: int):
        if len(self.openSlots()) == 0:
            self.endGame("Draw")
        
        # Check for vertical or horizontal wins
        for i in range(0, len(self.__board)):
            rows = all(self.__board[i, 0:] == playerNum)
            columns = all(self.__board[0:, i] == playerNum)
            if rows or columns:
                self.endGame(playerNum)
                self._winner = playerNum
                return
        
        diagonal1 = all(self.__board.diagonal() == playerNum)
        diagonal2 = all(fliplr(self.__board).diagonal() == playerNum)
        if diagonal1 or diagonal2:
            self.endGame(playerNum)
            self._winner = playerNum
            return 

    def endGame(self, winner: int):
        self.showBoard()
        if winner == 3:
            print('Draw!')
        elif winner == 0:
            print("You Win!")
        elif winner == 1:
            print("Computer won :(")
        self._gameOver = True
