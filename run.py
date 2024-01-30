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

    def check_hit(self, row, col):
        return self.start_row <= row <= self.end_row and self.start_col <= col <= self.end_col

    def is_sunk(self):
        length = (self.end_row - self.start_row + 1) * (self.end_col - self.start_col + 1)
        return self.hits == length


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

    def place_ship(self, ship):
        """ Place a ship on the board and mark its position""" 
        for r in range(ship.start_row, ship.end_row + 1):
            for c in range(ship.start_col, ship.end_col + 1):
                self.grid[r][c] = "O"
        self.ships.append(ship)

    def update_grid(self, row, col, hit):
        """ Define Hit and Missed on board""" 
        if hit:
            #its a hit!
            self.grid[row][col] = "X"
        else:
            #its a miss!
            self.grid[row][col] = "#"

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
        self.enemy_board = Board()
        self.tracking_board = Board()
        self.bullets_left = 50

    def place_ships(self, board, num_of_ships=8):
        """ Place a specified number of ships randomly on the board"""
        directions = ["left", "right", "up", "down"]
        for i in  range(num_of_ships):
            placed = False
            while not placed:
                row, col = random.randint(0, board.size - 1), random.randint(0, board.size - 1)
                direction = random.choice(directions)
                ship_size = random.randint(2, 4)
                placed = self.try_to_place_ship(board, row, col, direction, ship_size)

    def try_to_place_ship(self, board, row, col, direction, length):
        """ Try to place a ship on the board in the specified direction and length"""
        start_row, end_row = row, row  
        start_col, end_col = col, col

        if direction == "left":
            if col - length < 0:
                return False
            start_col = col - length
        elif direction == "right":
            if col + length > board.size:
                return False
            end_col = col + length - 1
        elif direction == "up":
            if row - length < 0:
                return False
            start_row = row - length
        elif direction == "down":
            if row + length > board.size:
                return False
            end_row = row + length - 1

        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                if board.grid[r][c] == "O":
                    return False

        ship = Ship(start_row, end_row, start_col, end_col)
        board.place_ship(ship)
        return True

    def get_shot_input(self):
        """ Receive and validate the players shot coordinates"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            try:
                shot = input("Enter row (A-J) and column (0-9) such as A3: ").upper()

                # Check if the input lenght is correct and characters are valid
                if len(shot) < 2 or len(shot) > 3:
                    raise ValueError("Invalid input length. Please enter in format A3.")
                if shot[0] not in alphabet or not shot[1:].isdigit():
                    raise ValueError("Invalid input format. Please enter in format A3.")

                row, col = alphabet.index(shot[0]), int(shot[1:])

                #Check if the row and column are within the board size
                if row >= self.enemy_board.size or col >self.enemy_board.size:
                    raise ValueError("Shot out of range. Please choose within A-J and 0-9.")

                return row, col

            except ValueError as e:
                print(e)

    def shoot(self, board, row, col, is_player_shooting=True):
        """ Determin wether a shot hits a ship and update the board accordingly"""
        hit = False
        for ship in board.ships: 
            if ship.check_hit(row, col):
                hit = True
                ship.hits += 1
                break
        
        if is_player_shooting:
            self.tracking_board.update_grid(row, col, hit)
        else:
            self.player_board.update_grid(row, col, hit)
        return hit

    def enemy_turn(self):
        row, col = random.randint(0, self.player_board.size - 1), random.randint(0, self.player_board.size - 1)
        print(f"Enemy shoots at ({row}, {col}): ", end= "")
        hit = self.shoot(self.enemy_board, row, col, is_player_shooting=False)
        print("Hit!" if hit else "Miss.") 

    def play(self):
        print("welcome to My Battleship Game!")
        self.place_ships(self.player_board)
        self.place_ships(self.enemy_board)

        print("\nPlayer Board:")
        self.player_board.print_board(hide_ships=False)
        print("\nTracking Board:")
        self.tracking_board.print_board(hide_ships=False)
        print(f"\nBullets left: {self.bullets_left}")

        row, col = self.get_shot_input()
        print(f"You shoot at ({row}, {col}): ", end="")
        if self.shoot(self.enemy_board, row, col, is_player_shooting=True):
            print("Hit!")
        else:
            print("Miss.")
        self.bullets_left -= 1

        self.enemy_turn()

""" Call the game functions """

game = Game()
game.play()