#This is my Milestone 1 from Udemy Python course
#using functions, control loops, and statements.
#Made by Thomas Chase October 7, 2020

#Functions

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def print_board(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

def x_movement(row1,row2,row3):
    row = int(input('Please enter the row you wish to place an X in: '))
    row = row-1
    column = int(input('Please enter the column you wish to plave an X in: '))
    column = column-1
    place_x(row,column,row1,row2,row3)
    return row1 and row2 and row3

def o_movement(row1,row2,row3):
    row = int(input('Please enter the row you wish to place a Y in: '))
    row = row-1
    column = int(input('Please enter the column you wish to place a Y in: '))
    column = column-1
    place_O(row,column,row1,row2,row3)
    return row1 and row2 and row3

def place_x(row,column,row1,row2,row3):
    if row == 0:
        row1[column] = 'X'
    elif row == 1:
        row2[column] = 'X'
    elif row == 2:
        row3[column] = 'X'
    return row1 and row2 and row3

def place_O(row,column,row1,row2,row3):
    if row == 0:
        row1[column] = 'O'
    elif row == 1:
        row2[column] = 'O'
    elif row == 2:
        row3[column] = 'O'
    return row1 and row2 and row3

def is_over():
    status = False
    awnser = input('Has there been a winner yet? (Y/N): ')

    if awnser == 'Y' or 'y':
        status = True
    else:
        stalemate = input('Is the game a stale mate? (Y/N) ')
        if stalemate == 'Y' or 'y':
            status = True
    return status

def start_game():
    print('Welcome to my Tic Tac Toe Game!')
    print('The first player will be X and the second will be O')
    print_board(row1,row2,row3)

def end_game():
    print('GAME OVER')

#Start of game script

start_game()

gameover = False #Flag for ending game
move = 0 # minimum of 4 movements before asking status

while gameover != True:

    x_movement(row1,row2,row3)
    print_board(row1,row2,row3)
    o_movement(row1,row2,row3)
    print_board(row1,row2,row3)
    move = move+1
    if move > 2:
        gameover = is_over()
    else:
        pass

end_game()

#END OF SCRIPT


