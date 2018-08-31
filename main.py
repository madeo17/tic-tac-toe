#! python3

# Tic Tac Toe game - my first project

import os
import random


def display_board(board):
    os.system('cls')
    print('|   |   |   |')
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print('|   |   |   |\n')


def player_input():
    choice = input('your move:')
    while not choice.isdigit() or not (0 < int(choice) < 10):
        choice = input('Invalid input. Try again:')
    return int(choice)


def place_marker(board, mark, position, three_in_line):
    board[position] = mark
    for i in three_in_line[mark]:
        if position in i:
            i.remove(position)


def win_check(mark, three_in_line):
    return [] in three_in_line[mark]


def choose_first():
    return random.choice(['X', 'O'])


def space_check(board, position):
    return ' ' == board[position]


def full_board_check(board):
    return ' ' not in board


def player_choice(board):
    choice = player_input()
    while not space_check(board, choice):
        print("This place isn't available.")
        choice = player_input()
    return choice


def winner(three_in_line):
    if [] in three_in_line['X']:
        return 'X'
    elif [] in three_in_line['O']:
        return 'O'
    else:
        return False


def replay():
    while True:
        choice = input('Do you want to play again? [Y/N]:')
        if choice.lower() == 'y':
            return True
        if choice.lower() == 'n':
            return False


def main():
    print('\nTIC TAC TOE\n')
    wanna_play = True
    while wanna_play:
        player_name = {'X': '', 'O': ''}
        print('Enter your names:')
        player_name['X'] = input('Player X:')
        player_name['O'] = input('Player O:')
        first_player = choose_first()
        second_player = 'X' if 'X' != first_player else 'O'
        print(f'\n{player_name[first_player]} will start.')
        input('Press Enter when ready...')
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
        three_in_line = {'X': [[7, 8, 9], [4, 5, 6], [1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]],
                         'O': [[7, 8, 9], [4, 5, 6], [1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]}
        display_board(board)
        while not full_board_check(board):
            print(f'{player_name[first_player]}, ', end='')
            place_marker(board, first_player,
                         player_choice(board), three_in_line)
            display_board(board)
            if win_check(first_player, three_in_line):
                break
            if full_board_check(board):
                break
            print(f'{player_name[second_player]}, ', end='')
            place_marker(board, second_player,
                         player_choice(board), three_in_line)
            display_board(board)
            if win_check(first_player, three_in_line):
                break
        if winner(three_in_line):
            print(
                f'Congratulations {player_name[winner(three_in_line)]}! You win!\n')
        else:
            print('TIE!')
        wanna_play = replay()
    print('Bye bye! Have a nice day!')


if __name__ == '__main__':
    main()
