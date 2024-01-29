# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Gameplan 
1. Its a 10x10 Board, with 8 ships of different lengths at random places
2. 2 Players with 50 shots each 
3. Players choose their shot coordinates and computer create the coordinate randomly
4. The Board will update to show misses and hits
5. Ships are places horizontaly and vertically.
"""



import random
import time

"""
Source: https://github.com/SaranSundar/PythonCurriculum/blob/main/Battleships/battleships_empty.py
I used this version of the game as a code base. Therfore, it has been modified and expanded by Michael Hirt for the purpose of this Project 3 - Python
"""


class Ship:
    def __init__(self, start_row, end_row, start_col, end_col):
        """ Initializes a ship with its position and hit counts """
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.hits = 0


class Board:
    def __init__(self, size=10):
        """ Initializes the game board with a given size""" 
        self.size = size
        self.grid = []
        for row in range(size):
            row_data = []
            for col in range(size):
                row_data.append(".")
            self.grid.append(row_data)
        self.ships = []

    def print_board(self, hide_ships=True):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(" " + " ".join(str(i) for i in range(self.size)))
        for row in range(self.size):
            row_display = [self.grid[row][col] if not hide_ships or self.grid[row][col] in ["X", "#"] else "." for col in range(self.size)]
            print(alphabet[row] + " " + " ".join(row_display))


class Game:
    def __init__(self):
        """ Print the current state of the game with the 2 boards"""
        self.player_board = Board()
        self.tracking_board = Board()
        self.bullets_left = 50

    def print_game_state(self):
        print("\nPlayer Board:")
        self.player_board.print_board(hide_ships=False)
        print("\nTracking Board:")
        self.tracking_board.print_board(hide_ships=False)
        print(f"\nBullets left: {self.bullets_left}")
   

""" Call the game functions """

game = Game()
game.print_game_state()