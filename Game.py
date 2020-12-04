import argparse
import multiprocessing as mp
import tkinter as tk
import argparse
import multiprocessing as mp
import tkinter as tk

# 3rd party libs
import numpy as np

# Local libs
#from Player import AIPlayer, RandomPlayer, HumanPlayer
from ChessPieces import King, Queen, Pawn, Knight, Bishop, Rook


def turn_worker(board, send_end, p_func):
    send_end.send(p_func(board))


class Game:
    def __init__(self, player1, player2, time):
        self.players = [player1, player2]
        self.colors = ['white', 'black']
        self.current_turn = 0
        self.board = np.zeros([8, 8]).astype(np.uint8)
        self.pieces = self.initializeBoard()
        self.gui_board = []
        self.game_over = False
        self.ai_turn_limit = time

    def make_move(self):
        pass

    def update_board(self, move, player_num):
        pass

    def game_completed(self, player_num):
        pass

    def initializeBoard(self):
        pieces = []
        for i in range(8):
            pawnWhite = Pawn("white", 1, i)
            pawnBlack = Pawn("black", 6, i)
            pieces.append(pawnWhite)
            pieces.append(pawnBlack)
        king = King("white", 0, 4)
        pieces.append(king)
        king = King("black", 7, 4)
        pieces.append(king)
        queen = Queen("white", 0, 3)
        pieces.append(queen)
        queen = Queen("black", 7, 3)
        pieces.append(queen)
        rook = Rook("white", 0, 0)
        pieces.append(rook)
        rook = Rook("white", 0, 7)
        pieces.append(rook)
        rook = Rook("black", 7, 0)
        pieces.append(rook)
        rook = Rook("black", 7, 7)
        pieces.append(rook)
        knight = Knight("white", 0, 1)
        pieces.append(knight)
        knight = Knight("white", 0, 6)
        pieces.append(knight)
        knight = Knight("black", 7, 1)
        pieces.append(knight)
        knight = Knight("black", 7, 6)
        pieces.append(knight)
        bishop = Bishop("white", 0, 2)
        pieces.append(bishop)
        bishop = Bishop("white", 0, 5)
        pieces.append(bishop)
        bishop = Bishop("black", 7, 2)
        pieces.append(bishop)
        bishop = Bishop("black", 7, 5)
        pieces.append(bishop)
        return pieces


def main(player1, player2, time):
    """
    Creates player objects based on the string paramters that are passed
    to it and calls play_game()

    INPUTS:
    player1 - a string ['ai', 'random', 'human']
    player2 - a string ['ai', 'random', 'human']
    """
    # def make_player(name, num):
    #     if name == 'ai':
    #         return AIPlayer(num)
    #     elif name == 'random':
    #         return RandomPlayer(num)
    #     elif name == 'human':
    #         return HumanPlayer(num)

    # Game(make_player(player1, 1), make_player(player2, 2), time)
    pass


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
