"""MAKING TIC TAC TOE BUT LAME!"""
from typing import Optional
import numpy as np
WHITE_BOX: str = "\U00002B1C"
DIAMOND: str = "\U00002665"
SPADE: str = "\U00002660"
grid: dict[int, str] = {
    1: WHITE_BOX,
    2: WHITE_BOX,
    3: WHITE_BOX,
    4: WHITE_BOX,
    5: WHITE_BOX,
    6: WHITE_BOX,
    7: WHITE_BOX,
    8: WHITE_BOX,
    9: WHITE_BOX
}

player_wins: list = []
cpu_wins: list = []
start: int = input("Welcome to Terminal Tic-Tac-Toe. As the player, you are the Spade. The CPU is the Diamond. "
                   "To start the game, enter 1")
cpu_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wins: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def player_turn(grid):
    move: int = int(input(f"Select an open position ({cpu_list[0]}-{cpu_list[len(cpu_list)-1]}): "))
    if move < 1 or move > 9:
        print("Input out of range. Enter an integer 1-9.")
        player_turn(grid)
    elif type(move) != int:
        print("Enter an integer 1-9.")
        player_turn(grid)
    if grid[int(move)] != WHITE_BOX:
        print("That position is taken. choose another.")
        player_turn(grid)
    else:
        grid[int(move)] = SPADE
        player_wins.append(move)
        cpu_list.remove(move)

def grid_string():
    thing = f"{grid[1]} {grid[2]} {grid[3]}\n" \
            f"{grid[4]} {grid[5]} {grid[6]}\n" \
            f"{grid[7]} {grid[8]} {grid[9]}"
    return thing


def cpu_turn(grid):
    move = np.random.choice(cpu_list)
    grid[int(move)] = DIAMOND
    cpu_list.remove(move)
    cpu_wins.append(move)


def win_condition(turn: list) -> bool:
    for condition in wins:
        count = 0
        j = 0
        for number in condition:
            found = False
            while j < len(turn):
                if np.sort(turn)[j] == number:
                    count += 1
                    found = True
                    break
                j += 1
            if found is False:
                break
        if count == 3:
           return True
    return False


def main() -> None:
    first_turn = np.random.choice(np.arange(0, 2))
    win = False
    i: int = 0
    turn = []
    while win is False and i < 10:
        if i == 9:
            break
        if first_turn == 0:
            player_turn(grid)
            turn = player_wins
            first_turn = 1
        elif first_turn == 1:
            cpu_turn(grid)
            turn = cpu_wins
            first_turn = 0
        if turn == player_wins:
            print(grid_string())
        if turn == cpu_wins and i ==1:
            print(grid_string())
        win = win_condition(turn)
        i += 1
    if win is True or i>=9:
        if i == 9 and win_condition is False:
            print("Tie!")
        elif turn == player_wins:
            print("You Won! Congrats.")
        else:
            print("Sorry, better luck next time.")


if __name__ == '__main__':
    main()


