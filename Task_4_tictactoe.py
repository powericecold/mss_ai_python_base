class Cell:
    def __init__(self):
        self._value = " "

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Board:
    def __init__(self):
        self.cells = [[Cell() for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.cells:
            print("|".join(cell.value for cell in row))
            print("-" * 5)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == " ":
                    return False
        return True

    def check_winner(self, player):
        # Check rows
        for row in self.cells:
            if all(cell.value == player.symbol for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.cells[row][col].value == player.symbol for row in range(3)):
                return True

        # Check diagonals
        if (self.cells[0][0].value == player.symbol and self.cells[1][1].value == player.symbol
                and self.cells[2][2].value == player.symbol):
            return True
        if (self.cells[0][2].value == player.symbol and self.cells[1][1].value == player.symbol
                and self.cells[2][0].value == player.symbol):
            return True

        return False


class Player:
    def __init__(self, symbol):
        self._symbol = symbol

    @property
    def symbol(self):
        return self._symbol


def play_game():
    board = Board()
    players = [Player("X"), Player("O")]
    current_player = players[0]

    print("Welcome to Tic-Tac-Toe!")
    print("To make a move, enter a number from 1 to 9 corresponding to the cell position:")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9\n")

    while not board.is_full():
        board.print_board()

        move = int(input(f"{current_player.symbol} - Enter your move (1-9): ")) - 1
        print('\n')
        row = move // 3
        col = move % 3

        if board.cells[row][col].value == " ":
            board.cells[row][col].value = current_player.symbol

            if board.check_winner(current_player):
                print(f"{current_player.symbol} wins!")
                break

            current_player = players[1] if current_player == players[0] else players[0]
        else:
            print("Invalid move. Try again.")

    if board.is_full():
        print("It's a tie!")

    board.print_board()


if __name__ == '__main__':
    play_game()
