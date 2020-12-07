import argparse
import multiprocessing as mp
import tkinter as tk
import argparse
import multiprocessing as mp
import tkinter as tk
import tkinter.font as tkFont

# 3rd party libs
import numpy as np

# Local libs
from Player import AIPlayer, RandomPlayer, HumanPlayer
from ChessPieces import King, Queen, Pawn, Knight, Bishop, Rook


def turn_worker(board, send_end, p_func):
    send_end.send(p_func(board))


class Game:
    def __init__(self, player1, player2, time):
        self.players = [player1, player2]
        self.colors = ['white', 'black']
        self.current_turn = 0
        self.board = [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
                      ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                      ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]
        self.pieces = [[Rook("black", 0, 0), Knight("black", 0, 1), Bishop("black", 0, 2), Queen("black", 0, 3), King("black", 0, 4), Bishop("black", 0, 5), Knight("black", 0, 6), Rook("black", 0, 7)],
                       [Pawn("black", 1, 0), Pawn("black", 1, 1), Pawn("black", 1, 2), Pawn("black", 1, 3), Pawn(
                           "black", 1, 4), Pawn("black", 1, 5), Pawn("black", 1, 6), Pawn("black", 1, 7)],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [Pawn("white", 6, 0), Pawn("white", 6, 1), Pawn("white", 6, 2), Pawn("white", 6, 3), Pawn(
                           "white", 6, 4), Pawn("white", 6, 5), Pawn("white", 6, 6), Pawn("white", 6, 7)],
                       [Rook("white", 7, 0), Knight("white", 7, 1), Bishop("white", 7, 2), Queen("white", 7, 3), King("white", 7, 4), Bishop("white", 7, 5), Knight("white", 7, 6), Rook("white", 7, 7)]]
        self.gui_piece = []
        self.gui_board = []
        self.game_over = False
        self.ai_turn_limit = time
        self.storedX = -1
        self.storedY = -1

        def movePiece(event):
            if(self.storedX == -1 and self.storedY == -1):
                self.storedX = int(event.y/100)
                self.storedY = int(event.x/100)
            else:
                piece = self.pieces[self.storedX][self.storedY]
                if(piece == None):
                    self.storedX = -1
                    self.storedY = -1
                    pass
                else:
                    newX = int(event.y/100)
                    newY = int(event.x/100)
                    if(piece.movePiece(newX, newY)):
                        self.pieces[self.storedX][self.storedY] = None
                        self.pieces[newX][newY] = piece
                        self.board[self.storedX][self.storedY] = '  '
                        self.board[newX][newY] = piece.getPieceCode()
                        self.storedX = -1
                        self.storedY = -1

                        white = True
                        for row in range(0, 800, 100):
                            column = []
                            for col in range(0, 800, 100):
                                color = ''
                                if(white):
                                    color = '#eeeed2'
                                else:
                                    color = '#663300'
                                column.append(self.c.create_rectangle(
                                    row, col, row+100, col+100, fill=color))
                                white = not white
                            self.gui_board.append(column)
                            white = not white

                        for row in range(0, 800, 100):
                            # column = []
                            for col in range(0, 800, 100):
                                if(not self.board[int(row/100)][int(col/100)] == '  '):
                                    self.piece = tk.PhotoImage(
                                        file='./chesspieceicons/%s.png' % self.board[int(row/100)][int(col/100)])
                                    self.gui_piece.append(self.piece)
                                    self.c.image_names = self.piece
                                    self.c.create_image(
                                        col, row+5, image=self.piece, state=tk.NORMAL, anchor=tk.NW, tag='piece')
                        root.mainloop()
                    else:
                        self.storedY = -1
                        self.storedX = -1

        root = tk.Tk()
        root.title('Chess')
        self.player_string = tk.Label(root, text=player1.player_string)
        self.player_string.pack()
        self.c = tk.Canvas(root, width=800, height=800)
        self.c.bind("<Button-1>", movePiece)
        self.c.pack()
        self.piece = None

        white = True
        for row in range(0, 800, 100):
            column = []
            for col in range(0, 800, 100):
                color = ''
                if(white):
                    color = '#eeeed2'
                else:
                    color = '#663300'
                column.append(self.c.create_rectangle(
                    row, col, row+100, col+100, fill=color))
                white = not white
            self.gui_board.append(column)
            white = not white

        for row in range(0, 800, 100):
            # column = []
            for col in range(0, 800, 100):
                if(not self.board[int(row/100)][int(col/100)] == '  '):
                    self.piece = tk.PhotoImage(
                        file='./chesspieceicons/%s.png' % self.board[int(row/100)][int(col/100)])
                    self.gui_piece.append(self.piece)
                    self.c.image_names = self.piece
                    self.c.create_image(
                        col, row+5, image=self.piece, state=tk.NORMAL, anchor=tk.NW, tag='piece')

        root.mainloop()

    def make_move(self):
        pass

    def update_board(self, move, player_num):
        pass

    def game_completed(self, player_num):
        pass


def main(player1, player2, time):
    """
    Creates player objects based on the string paramters that are passed
    to it and calls play_game()

    INPUTS:
    player1 - a string ['ai', 'random', 'human']
    player2 - a string ['ai', 'random', 'human']
    """
    def make_player(name, num):
        if name == 'ai':
            return AIPlayer(num)
        elif name == 'random':
            return RandomPlayer(num)
        elif name == 'human':
            return HumanPlayer(num)

    Game(make_player(player1, 1), make_player(player2, 2), time)


def play_game(player1, player2):
    """
    Creates a new game GUI and plays a game using the two players passed in.

    INPUTS:
    - player1 an object of type AIPlayer, RandomPlayer, or HumanPlayer
    - player2 an object of type AIPlayer, RandomPlayer, or HumanPlayer

    RETURNS:
    None
    """
    board = np.zeros([8, 8])


if __name__ == '__main__':
    player_types = ['ai', 'random', 'human']
    parser = argparse.ArgumentParser()
    parser.add_argument('player1', choices=player_types)
    parser.add_argument('player2', choices=player_types)
    parser.add_argument('--time',
                        type=int,
                        default=60,
                        help='Time to wait for a move in seconds (int)')
    args = parser.parse_args()

    main(args.player1, args.player2, args.time)
