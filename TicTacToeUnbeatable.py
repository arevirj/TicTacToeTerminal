"""MAKING TIC TAC TOE BUT LAME!"""
import numpy as np
import copy
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
empty_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wins: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def player_turn(grid):
    move: int = int(input(f"Select an open position: "))
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
        empty_list.remove(move)


def grid_string():
    thing = f"{grid[1]} {grid[2]} {grid[3]}\n" \
            f"{grid[4]} {grid[5]} {grid[6]}\n" \
            f"{grid[7]} {grid[8]} {grid[9]}"
    return thing


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


def minimax(board: dict, empty: list, maximum):
    # Terminal states, lose, win , tie.
    if win_condition(player_wins):
        return -10
    elif win_condition(cpu_wins):
        return 10
    elif len(empty) == 0:
        return 0
    else:
        if maximum is True:
            best_score = -1000
            new_board = copy.deepcopy(board)
            #empties = empty[:]
            for spot in empty:
                cpu_wins.append(spot)
                temp = empty[:]
                temp.remove(spot)
                #empties.remove(spot)
                new_board[spot] = DIAMOND
                score = minimax(new_board, temp, False)
                cpu_wins.remove(spot)
                if score > best_score:
                    best_score = score
        else:
            best_score = 1000
            new_board = copy.deepcopy(board)
            #empties = empty[:]
            for spot in empty:
                player_wins.append(spot)
                temp = empty[:]
                temp.remove(spot)
                new_board[spot] = SPADE
                score = minimax(new_board, temp, True)
                player_wins.remove(spot)
                if score < best_score:
                    best_score = score
        return best_score


def cpu_turn(grid, cpu_wins):
    if len(player_wins) == 0 and len(cpu_wins) == 0:
        grid[1] = DIAMOND
        cpu_wins.append(1)
        empty_list.remove(1)
    else:
        best_score = -1000
        best_move = 0

        score = best_score
        for spot in empty_list:
            grid[spot] = DIAMOND
            cpu_wins.append(spot)
            temp = empty_list[:]
            temp.remove(spot)
            score = minimax(grid, temp, False)
            grid[spot] = EMPTY
            cpu_wins.remove(spot)
            if score > best_score:
                best_score = score
                best_move = spot
        grid[best_move] = DIAMOND
        cpu_wins.append(best_move)
        empty_list.remove(best_move)
        return

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
            cpu_turn(grid, cpu_wins)
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


