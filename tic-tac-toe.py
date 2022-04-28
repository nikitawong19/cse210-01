'''
Tic-Tac-Toe game.
Author: Nikita Wong
'''

# Call the main to execute all the code.
def main():

    # Display the board.
    display_board()

    # If the game still going will repeat the following action.
    while game_still_going:
        handle_turn(current_player) 
        check_if_game_over()
        flip_player()

    # If the game has ended, print either X or O won.
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')      


# Set global variables so that the variable can be used everywhere.
game_still_going = True
winner = None
current_player = 'X'


# Game board.
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']


# Display the game board.
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Handle a single turn of an arbitrary player.
def handle_turn(player): 

    # Show which player's turn.
    print(player + "'s' turn.")

    # Ask user for input.
    position = input('Choose a position from 1-9: ')

    print()

    valid = False

    while not valid: 

        # Check if the input is in this list (1-9). If not, keep asking the user for valid input until valid input.
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Choose a position from 1-9: ')
            
        # Positon is 1-9, but the element in the list is 0-8. 
        # If we get position 1, what we actually want is 0. 
        # So we substract 1 so that we know where the position go in the board.
        position = int(position) - 1

        # Check if the board position is available or empty spot.
        if board[position] == '-': 
            valid = True # If the board position is available,
        else: # If the board position is not available, it will print error message.
            print("You can't go there. Try again.")


    board[position] = player # then place the position on the board.

    display_board()


# Check if the game has ended.
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check for winner.
def check_for_winner():

    # Set up global variable.
    global winner

    # Check rows
    row_winner = check_rows()

    # Check columns
    column_winner = check_columns()

    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


# Check rows for winner.
def check_rows(): 

    # Set up global variable.
    global game_still_going

     # Check if any of the rows have all the same value and not empty '-'.
    row_1_win = board[0] == board[1] == board[2] != '-'
    row_2_win = board[3] == board[4] == board[5] != '-'
    row_3_win = board[6] == board[7] == board[8] != '-'

    # If any row does have a match, then stop the game.
    if row_1_win or row_2_win or row_3_win:
        game_still_going = False # Stop the game.

    # We know there is a win in the row, but don't know who is the winner so check individually.
    if row_1_win:
        return board[0] # If board[0] is X, X is the winner, and vise versa.
    elif row_2_win:
        return board[3] # If board[3] is X, X is the winner, and vise versa.
    elif row_3_win:
        return board[6] # If board[6] is X, X is the winner, and vise versa.
    return


# Check columns for winner.
def check_columns(): 
    
    # Set up global variable.
    global game_still_going

    # Check if any of the columns have all the same value and is not empty '-'.
    column_1_win = board[0] == board[3] == board[6] != '-'
    column_2_win = board[1] == board[4] == board[7] != '-'
    column_3_win = board[2] == board[5] == board[8] != '-'

    # If any columns does have a match, then stop the game.
    if column_1_win or column_2_win or column_3_win:
        game_still_going = False # Stop the game.

    # We know there is a win in the column, but don't know who is the winner so check individually.
    if column_1_win:
        return board[0] # If board[0] is X, X is the winner, and vise versa.
    elif column_2_win:
        return board[1] # If board[1] is X, X is the winner, and vise versa.
    elif column_3_win:
        return board[2] # If board[2] is X, X is the winner, and vise versa.
    return


# Check diagonals for winner.
def check_diagonals(): 

    # Set up global variable.
    global game_still_going

    # Check if any of the columns have all the same value and is not empty '-'.
    diagonals_1_win = board[0] == board[4] == board[8] != '-'
    diagonals_2_win = board[6] == board[4] == board[2] != '-'

    # If any diagonals does have a match, then stop the game.
    if diagonals_1_win or diagonals_2_win:
        game_still_going = False # Stop the game.

    # We know there is a win in the diagonals, but don't know who is the winner so check individually.
    if diagonals_1_win:
        return board[0] # If board[0] is X, X is the winner, and vise versa.
    elif diagonals_2_win:
        return board[6] # If board[6] is X, X is the winner, and vise versa.
    return

# Check if tie.
def check_if_tie():

    # Set up global variable.
    global game_still_going

    # If no more empty spot on the board, then stop the game.
    if '-' not in board:
        game_still_going = False
    return


# Flip player.
def flip_player(): 

    # Set up global variable.
    global current_player

    # If the current player is X, then change it to O and vise versa.
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return  


# If this file is executed like this: tic-tac-toe.py, then call the main function. 
# However, if the file is simply imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()