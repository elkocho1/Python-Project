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
Create the game for a single player 
Source: https://github.com/SaranSundar/PythonCurriculum/blob/main/Battleships/battleships_empty.py
This version has been modified and expanded upon by Michael Hirt for the purpose of this Project 3 - Python
"""

board = [[]]
board_size = 10
num_of_ships = 8
shots_left = 50
game_over = False
num_of_ships_sunk = 0
ship_positions = [[]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_ship_placement(start_row, end_row, start_col, end_col):
    """
    Check if a ship can be placed in specific area. Returns True if placement is possible otherwise False

    """
    global board
    global ship_positions
