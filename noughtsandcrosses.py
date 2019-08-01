class Board:
    SYMBOLS = ('O', 'X')
    LINES = (
        # horizontal
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # vertical
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # diagonal
        (0, 4, 8),
        (2, 4, 6)
    )

    def __init__(self):
        self.spaces = [None] * 9
    
    def place(self, position, playernum):
        if self.spaces[position] != None:
            print("That space is occupied!")
            return False
        else:
            self.spaces[position] = playernum
            return True

    def fmt_space(self, playernum):
        return ' ' if playernum is None else self.SYMBOLS[playernum]

    def draw(self):
        print("""
        + - - - +
        | {0} {1} {2} |
        | {3} {4} {5} |
        | {6} {7} {8} |
        + - - - +
        """.format(*[self.fmt_space(self.spaces[s]) for s in range(9)]))

    def check_winner(self):
        for line in self.LINES:
            entries = (self.spaces[line[0]], self.spaces[line[1]], self.spaces[line[2]])
            if None in entries:
                continue
            if entries[0] == entries[1] and entries[1] == entries[2]:
                return entries[0]
        return None

def play():
    board = Board()

    toggle = False
    while True:
        player = int(toggle)
        board.draw()
        print(f"Player {player + 1}'s ({Board.SYMBOLS[player]}) turn")
        valid = False
        while not valid:
            move = int(input("Input a position (1-9): "))
            valid = board.place(move - 1, player)
        winner = board.check_winner()
        if winner != None:
            board.draw()
            print(f"Player {winner} has won the game!")
            break
        toggle = not toggle

if __name__ == "__main__":
    play()

