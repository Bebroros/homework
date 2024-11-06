class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.place = (x, y)


class Pawn(Piece):
    def __init__(self, color, x, y, name='Pawn'):
        super().__init__(color, x, y)
        self.name = name

    def move(self, move):
        if (self.place[1] + 1) < 9 and move == (0, 1):
            self.place = (self.place[0], self.place[1] + move[1])
            return True
        else:
            return False


class Knigth(Piece):
    def __init__(self, color, x, y, name='Knigth'):
        super().__init__(color, x, y)
        self.name = name

    def move(self, move):
        if (0 < (self.place[1] + move[1]) < 9) \
                and (0 < (self.place[0] + move[0]) < 9) \
                and ((abs(move[1]) == 2 and abs(move[0] == 1)) or (abs(move[1]) == 1 and abs(move[0]) == 1)):
            self.place = (self.place[0] + move[0], self.place[1] + move[1])
            return True
        else:
            return False


class Bishop(Piece):
    def __init__(self, color, x, y, name='Bishop'):
        super().__init__(color, x, y)
        self.name = name

    def move(self, move):
        if (0 < (self.place[1] + move[1]) < 9) and (0 < (self.place[0] + move[0]) < 9) \
                and (abs(move[0]) == abs(move[1])):
            self.place = (self.place[0] + move[0], self.place[1] + move[1])
            return True
        else:
            return False


class Rook(Piece):
    def __init__(self, color, x, y, name='Rook'):
        super().__init__(color, x, y)
        self.name = name

    def move(self, move):
        if (0 < (self.place[1] + move[1]) < 9) and (0 < (self.place[0] + move[0]) < 9) \
                and (abs(move[1] == 0 or abs(move[0] == 0))):
            self.place = (self.place[0] + move[0], self.place[1] + move[1])
            return True
        else:
            return False


class Queen(Piece):
    def __init__(self, color, x, y, name='Queen'):
        super().__init__(color, x, y)
        self.name = name

    def move(self, move):
        if (0 < (self.place[1] + move[1]) < 9) and (0 < (self.place[0] + move[0]) < 9) \
                and ((abs(move[1] == 0 or abs(move[0] == 0))) or (abs(move[0]) == abs(move[1]))):
            self.place = (self.place[0] + move[0], self.place[1] + move[1])
            return True
        else:
            return False


class King(Piece):
    def __init__(self, color, x, y, name='King'):
        super().__init__(color, x, y)
        self.name = name

    def move(self, move):
        if ((0 < (self.place[1] + move[1]) < 9) and (0 < (self.place[0] + move[0]) < 9)
                and (0 <= abs(move[0]) <= 1) and (0 <= abs(move[1]) <= 1)):
            self.place = (self.place[0] + move[0], self.place[1] + move[1])
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.board = {}

    def place_piece(self, piece):
        if not self.board.get(piece.place):
            self.board[piece.place] = piece.name
        else:
            print('There is a piece already on this place')

    def remove_piece(self, piece):
        if self.board.get(piece.place):
            del self.board[piece.place]
        else:
            print('There is no piece on this place')

    def move_piece(self, piece, move):
        if self.board[piece.place] == piece.name:
            self.remove_piece(piece)
            if piece.move(move):
                self.place_piece(piece)
                return True
            else:
                self.place_piece(piece)
                print("Piece can't move like this")
                return False

    def get_piece_at_position(self, piece, place):
        if not self.board.get(piece.place):
            self.remove_piece(piece)
            piece.place = place
            self.place_piece(piece)

    def get_all_pieces(self):
        for place in self.board:
            print(f'{place}: {self.board[place]}')

    def is_valid_move(self, piece, move):
        old_place = piece.place
        if self.move_piece(piece, move):
            print('Piece can be moved this way')
            self.remove_piece(piece)
            piece.place = old_place
            self.place_piece(piece)


def main():
    board = Board()
    pawn = Pawn('white', 1, 2)
    board.place_piece(pawn)
    board.get_all_pieces()
    board.move_piece(pawn, (0, 1))
    pawn.move((0, 1))
    board.get_all_pieces()
    rook = Rook('white', 2, 3)
    board.place_piece(rook)
    board.get_all_pieces()
    board.move_piece(rook, (3, 0))
    board.get_all_pieces()
    board.is_valid_move(rook, (6, 1))
    board.get_all_pieces()


if __name__ == '__main__':
    main()
