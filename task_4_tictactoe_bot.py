import random


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
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # Top row
            [(1, 0), (1, 1), (1, 2)],  # Middle row
            [(2, 0), (2, 1), (2, 2)],  # Bottom row
            [(0, 0), (1, 0), (2, 0)],  # Left column
            [(0, 1), (1, 1), (2, 1)],  # Middle column
            [(0, 2), (1, 2), (2, 2)],  # Right column
            [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
            [(0, 2), (1, 1), (2, 0)]   # Diagonal from top-right to bottom-left
        ]

        for combination in winning_combinations:
            if all(self.cells[row][col].value == player.symbol for row, col in combination):
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
    first_player = random.choice(players)
    current_player = first_player

    print("Welcome to Tic-Tac-Toe!")
    print("To make a move, enter a number from 1 to 9 corresponding to the cell position:")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")
    print(f"{first_player.symbol} starts first!")

    while not board.is_full():
        board.print_board()

        if current_player == players[0]:
            valid_move = False
            while not valid_move:
                move = int(input(f"{current_player.symbol} - Enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid move. Try again.")
                else:
                    row = move // 3
                    col = move % 3
                    if board.cells[row][col].value == " ":
                        valid_move = True
                    else:
                        print("Invalid move. Try again.")
        else:
            empty_cells = [(i, j) for i in range(3) for j in range(3) if board.cells[i][j].value == " "]
            row, col = random.choice(empty_cells)

        board.cells[row][col].value = current_player.symbol

        if board.check_winner(current_player):
            print(f"{current_player.symbol} wins!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

    if board.is_full():
        print("It's a tie!")

    board.print_board()


if __name__ == '__main__':
    play_game()
