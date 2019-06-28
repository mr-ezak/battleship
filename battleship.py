#Name: Battleship Game
#Description: A simple Battleship game that will allow you to specify your ships locations yourslef.
#Author: Mr Ezak

#Variables
board = []
damaged = []
turn = 0

# The locations of our ships
# 5 point Ships
ship1 = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
ship2 = [[4, 1], [4, 2], [4, 3], [4, 4], [4, 5]]

# 3 point Ships
ship3 = [[1, 7], [2, 7], [3, 7]]
ship4 = [[5, 7], [6, 7], [7 ,7]]

# 2 point Ships
ship5 = [[2, 8], [2, 9]]
ship6 = [[4, 8], [4, 9]]
ship7 = [[6, 8], [6, 9]]

# The array that contain all of our ships locations in one place
shiplist = [ship1[0], ship1[1], ship1[2], ship1[3], ship1[4], ship2[0], ship2[1], ship2[2], ship2[3], ship2[4], ship3[0], ship3[1], ship3[2], ship4[0], ship4[1], ship4[2], ship5[0], ship5[1], ship6[0], ship6[1], ship7[0], ship7[1]]

#Creating our 10*10 board
for x in range(10):
    board.append(["~"] * 10)

def print_board(board):
    for row in board:
        print((" ").join(row))

#Start the game by printing a message and creat our board
print("Let's play Battleship!")
print_board(board)

