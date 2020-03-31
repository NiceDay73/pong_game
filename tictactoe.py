'''
Simple Tic Tac Toe game for 2 players at the same computer
'''
import time


def display_game(game, player_1, player_2, wins):
    ''' Function to display the game board.
        INPUT: A list with the values at every position of the board
               2 strings correspondong to the marks choosen by player 1 and 2
               A dictionary with the count of victories for each player
    '''
    print('\n' * 80)
    print('*' * 21)
    print('*    TIC TAC TOE    *')
    print('*' * 21)
    print()
    print(f'PLAYER 1({player_1}): {wins[player_1]} victories')
    print(f'PLAYER 2({player_2}): {wins[player_2]} victories')
    print()
    print('  Positions          Board')
    print('  ---------          -----')
    print()
    print(f' 7 | 8 | 9         {game[7]} | {game[8]} | {game[9]} ')
    print('---+---+---       ---+---+---')
    print(f' 4 | 5 | 6         {game[4]} | {game[5]} | {game[6]} ')
    print('---+---+---       ---+---+---')
    print(f' 1 | 2 | 3         {game[1]} | {game[2]} | {game[3]} ')
    print('           ')


def choose_mark():
    while True:
        print('\n' * 100)
        player_1 = input('Player 1, choose your mark(X/O): ')
        player_1 = player_1.upper()
        if player_1 == 'X' or player_1 == 'O':
            break

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    return (player_1, player_2)


def choose_position(game, player):
    while True:
        pos = input(f'Player {player}: Choose your play(1-9)? ')
        if len(pos) == 1 and pos in ('123456789') and game[int(pos)] == ' ':
            print('Try another position!!!')
            break
    return int(pos)


def validate_winner(game):
    if ((game[1] != ' ' and game[1] == game[2] and game[1] == game[3])           # bottom line
            or (game[4] != ' ' and game[4] == game[5] == game[6])    # middle line
            or (game[7] != ' ' and game[7] == game[8] == game[8])    # top line
            or (game[1] != ' ' and game[1] == game[4] == game[7])    # first column
            or (game[2] != ' ' and game[2] == game[5] == game[8])    # second column
            or (game[3] != ' ' and game[3] == game[6] == game[9])    # third column
            or (game[3] != ' ' and game[3] == game[5] == game[7])    # diagonal bottom right to top left
            or (game[1] != ' ' and game[1] == game[5] == game[9])):  # diagonal bottom left to top right
        return True
    else:
        return False


def main():
    players = tuple(choose_mark())
    wins = {'X': 0, 'O': 0}

    while True:
        while True:
            play_again = input('Do you want to play(y/n)?')
            if play_again == 'y' or play_again == 'n':
                break
        # exits the loop and end the game
        if play_again == 'n':
            break

        game = ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        player = 0
        # loop is running until someone wins the game
        winner = False
        display_game(game, players[0], players[1], wins)
        while True:
            pos = choose_position(game, players[player])
            # put the mark in the game board
            game[pos] = players[player]
            display_game(game, players[0], players[1], wins)
            winner = validate_winner(game)
            # if there is a winner, increment the victories counter and exits the loop without initialize the player,
            # so the loser starts the new game
            if winner:
                wins[players[player]] += 1
                display_game(game, players[0], players[1], wins)
                print(f'Player {players[player]} WINS!!!!')
                break
            player = (player + 1) % 2
            if not ' ' in game:
                display_game(game, players[0], players[1], wins)
                print('THERE IS NO WINNER THIS TIME!!! TRY AGAIN')
                time.sleep(2)
                break


if __name__ == '__main__':
    main()
