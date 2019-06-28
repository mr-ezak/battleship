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

while(1):
    print("turn: ",turn)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    hisguess = [guess_row, guess_col]
    dmg = 0
    count = 0

    if(guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
        print("\n------------------\nOops, that's not even in the ocean.\n------------------\n")
    elif (board[guess_row][guess_col] == "X"):
        print("\n------------------\nYou hit that one already.\n------------------\n")
    else:
        for item in shiplist:
            myship = int("".join(map(num, item)))
            fire = int("".join(map(num, hisguess)))
            
            if (myship == fire):
                if damaged:
                    for damage in damaged:
                        hisdamage = int("".join(map(str, damage)))
                        if (fire == hisdamage):
                            dmg += 1
                    if(dmg == 0):
                        board[guess_row][guess_col] = "X"
                        damaged.append([guess_row, guess_col])
                        count += 1
                else:
                    board[guess_row][guess_col] = "X"
                    damaged.append([guess_row, guess_col])
                    count += 1
        if(count>0):
            print("\n----- * * * -----\nNice Shot, You hit a target!\n----- * * * -----\n")
        elif(dmg>0):
            print("\n------------------\nYou hit that place already.\n------------------\n")
        else:
            print("\n----- * * * -----\nMissed, Pay more atention please!\n----- * * * -----\n")
        if (len(damaged) == 22):
            print("\n----- * * * -----\n Good Job Soldier, You killed them all with ",turn+1," shots","\n----- * * * -----\n")
            break
    turn += 1
    print_board(board)