"""MAKING TIC TAC TOE BUT LAME!"""
from typing import Optional
import numpy as np
EMPTY: str = "\U00002B1C"
DIAMOND: str = "\U00002665"
SPADE: str = "\U00002660"
grid: dict[int, str] = {
    1: EMPTY,
    2: EMPTY,
    3: EMPTY,
    4: EMPTY,
    5: EMPTY,
    6: EMPTY,
    7: EMPTY,
    8: EMPTY,
    9: EMPTY
}
player_wins: list = []
cpu_wins: list = []
start: int = int(input("Welcome to Terminal Tic-Tac-Toe. As the player, you are the Spade. The CPU is the Diamond. "
                        "To start the game, enter 1: "))
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
    if grid[int(move)] != EMPTY:
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


def cpu_turn(grid, turn: list):
    if grid[5] == EMPTY:
        move = 5
        cpu_list.remove(move)
        cpu_wins.append(move)
        return move
    elif len(turn) == 1 and grid[5] != EMPTY:
        corners = [1, 3, 7, 9]
        for i in corners:
            if grid[i] == EMPTY:
                move = i
        cpu_list.remove(move)
        cpu_wins.append(move)
        return move
    else:
        for condition in wins:
            count = 0
            j = 0
            temp: list = []
            cond_temp: list = []
            for number in condition:
                found = False
                while j < len(turn):
                    if np.sort(turn)[j] == number:
                        count += 1
                        temp.append(number)
                        print(temp)
                        found = True
                        j += 1
                        break
                    j += 1
                if found is False:
                    break
            if count == 2:
                cond_temp = condition[:]
                print(cond_temp)
                cond_temp.remove(temp[0])
                cond_temp.remove(temp[1])
                if grid[cond_temp[0]] == EMPTY:
                    move = cond_temp[0]
                    print(cond_temp[0])
                    cpu_list.remove(move)
                    cpu_wins.append(move)
                    return move
        if turn == cpu_wins:
            return 15
        elif turn == player_wins:
            print("Random")
            move = np.random.choice(cpu_list)
            cpu_list.remove(move)
            cpu_wins.append(move)
            return move




def win_condition(turn: list) -> bool:
    for condition in wins:
        count = 0
        j = 0
        for number in condition:
            found = False
            while j < len(turn):
                if np.sort(turn)[j] == number:
                    count += 1
                    print(number)
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
    print(grid_string())
    while win is False and i < 10:
        if i == 9:
            break
        if first_turn == 0:
            player_turn(grid)
            turn = player_wins
            first_turn = 1
        elif first_turn == 1:
            play_check = cpu_turn(grid, cpu_wins)
            if  play_check != 15:
                grid[play_check] = DIAMOND
                print(f"used cpu list move: {play_check}")
            else:
                print("switch")
                cpu_check = cpu_turn(grid, player_wins)
                grid[cpu_check] = DIAMOND
                print(f"used player list move: {cpu_check}")
            turn = cpu_wins
            first_turn = 0
        print("------------")
        print(grid_string())
        if turn == cpu_wins:
            print("CPU Move")
        win = win_condition(turn)
        i += 1
    if win is True or i >= 9:
        if i == 9 and win is False:
            print("Tie!")
        elif turn == player_wins:
            print("You Won! Congrats.")
        else:
            print("Sorry, better luck next time.")


if __name__ == '__main__':
    main()


