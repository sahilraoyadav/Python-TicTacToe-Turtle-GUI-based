"""
Name - Sahil Yadav
Class - CSC 131 008
Project - TicTacToe Turtle Assignment 3
Description - This is a game called TicTacToe, which is like connect the dots but with only 3 dots :). This game is a two player game and user can play as many time as they prefer.
              This game has a graphic board which was created by using turtle to show the results rather than tex based result. 
"""
#imports turtle
import turtle

# Intial board with '-' for user to fill in.
board = ["-"] * 10
# Board with position for user to use as refernce board.
position = [None] + list(range(1, 10))


# Draws boards for the game. 
def drawBoard(board):
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])
    print()


# Checks user input and is it valid or not.
def getMove(board, name):
    while True:
        try:
            user_input = int(input(name + " it's your turn. Enter a move (1 - 9) "))
            if user_input < 1 or user_input > 9 or board[user_input] != '-':
                print(" Invalid move. Please try again using the position chart below! ")
                drawBoard(position)
            else:
                return user_input
        except ValueError:
            print("\nThat is not a number. Try again!")


# Checks if user won.
def win(board, symbol):
    # The winning combinations in all directions.
    return ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or  # across the bottom
            (board[4] == symbol and board[5] == symbol and board[6] == symbol) or  # across the middle
            (board[1] == symbol and board[2] == symbol and board[3] == symbol) or  # across the top
            (board[7] == symbol and board[4] == symbol and board[1] == symbol) or  # down the left side
            (board[8] == symbol and board[5] == symbol and board[2] == symbol) or  # down the middle
            (board[9] == symbol and board[6] == symbol and board[3] == symbol) or  # down the right side
            (board[7] == symbol and board[5] == symbol and board[3] == symbol) or  # diagonal
            (board[9] == symbol and board[5] == symbol and board[1] == symbol))  # diagonal


# Checks if the game ends in a tie.
def tie(board):
    for i in board:
        if i == '-':
            return False
    return True

# Sets up the tac board using turtle.
def setupboard(tac_board):
    #Speed of turtle
    tac_board.speed(50)
    #Width and color of the lines on the board
    tac_board.width(5)
    tac_board.pencolor("navy blue")
    #Hides the turtle
    tac_board.hideturtle()
    #Makes the tic tac toe board
    tac_board.penup()
    tac_board.goto(90, 300)
    tac_board.pendown()
    tac_board.setheading(270)
    tac_board.forward(600)
    tac_board.penup()
    tac_board.goto(-90, 300)
    tac_board.pendown()
    tac_board.forward(600)
    tac_board.penup()
    tac_board.goto(-300, 90)
    tac_board.pendown()
    tac_board.lt(90)
    tac_board.forward(600)
    tac_board.penup()
    tac_board.goto(-300, -90)
    tac_board.pendown()
    tac_board.forward(600)

"""Function takes in the user input and displays a X or O on the turtle tic tac toe board.
It uses position assigned to each number in the if loop to locate where to print the object."""
def turtleDrawBoard(board, tac_board, user_input, user):
    tac_board.penup()
    tac_board.hideturtle()
    if user_input == 1:
        tac_board.goto(-200, 120)
    elif user_input == 2:
        tac_board.goto(0, 120)
    elif user_input == 3:
        tac_board.goto(200, 120)
    elif user_input == 4:
        tac_board.goto(-200, -80)
    elif user_input == 5:
        tac_board.goto(0, -80)
    elif user_input == 6:
        tac_board.goto(200, -80)
    elif user_input == 7:
        tac_board.goto(-200, -270)
    elif user_input == 8:
        tac_board.goto(0, -270)
    else:
        tac_board.goto(200, -260)
    # calls drawShape which uses the user_input and then draws user symbol.
    drawShape(tac_board, user)

#Makes and prints the objeect X or O according to the user symbol and then sends it to turtleDrawBoard() to find a location based on user input. 
def drawShape(tac_board, user):
    #Makes the object x or o by using turtle
    if user == "X":
        tac_board.hideturtle()
        tac_board.speed(10)
        tac_board.width(10)
        tac_board.pencolor("teal")
        tac_board.setheading(90)
        tac_board.forward(70)
        tac_board.pendown()
        tac_board.setheading(45)
        for i in range(4):
            tac_board.back(100)
            tac_board.forward(100)
            tac_board.rt(90)
        tac_board.penup()
        tac_board.setheading(270)
        tac_board.forward(80)
        tac_board.setheading(0)
    else:
        tac_board.width(10)
        tac_board.pencolor("gold")
        tac_board.pendown()
        tac_board.circle(80)

""" Main function. It first prints out the statement to ask for user name and then uses per defined symbols to assign the user to a symbol. Then the function prints out position board and
game board. Then it checks the user inputs until player 1 or player 2 has won or tied or lost the game."""


def main():
    #Sets up the window for the turtle
    turtle.setup(640, 640)
    #creates the turtle
    tac_board = turtle.Turtle()
    setupboard(tac_board)
    print("Let's play TicTacToe. \n")
    # User inputs
    player1 = input("Enter the name of player 1: \n")
    player2 = input("Enter the name of player 2: \n")
    # Per-defined user symbols 
    player1_symbol = 'X'
    player2_symbol = 'O'
    #prints out the symbols to let the user know what symbol they are
    print("\n" + player1 + " you are: " + player1_symbol)
    print("\n" + player2 + " you are: " + player2_symbol)
    # Shows position board and the game board
    print("\nEnter your marks using the board positions shown below:")
    drawBoard(position)
    print("\nGame board")
    drawBoard(board)
    # Checks both of the user inputs until the game is won or tied. 
    while True: 
        # Player 1 input.
        user_input = getMove(board, player1)
        board[user_input] = player1_symbol
        drawBoard(board)
        #draws the board with player 1 move on the board
        turtleDrawBoard(board, tac_board, user_input, player1_symbol)

        # Checks if the player1 won.
        if win(board, player1_symbol):
            print(player1 + " wins!")
            break
        # Checks if the game is tied.
        if tie(board):
            print("Tie game!")
            break
        # Player 2 input.
        user_input = getMove(board, player2)
        board[user_input] = player2_symbol
        drawBoard(board)
        #draws the board with player 2 move on the board
        turtleDrawBoard(board, tac_board, user_input, player2_symbol)

        # Checks if the player2 won.
        if win(board, player2_symbol):
            print(player2 + " wins!")
            break
        # Checks if the game is tied.
        if tie(board):
            print("Tie game!")
            break


# Checks if everthing works and then it runs.
while True:
    # Calls the main funcion after checking everything is true
    main()
    # Restart the game!
    if input("Do you want to play again (y or n)?") != 'y':
        break
    # Resets the game if user presses y!
    board = ["-"] * 10
    drawBoard(board)
