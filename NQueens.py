"""
this script solves the n queen problem
using back_tracking and draw the board
"""
iteration = 0


def create_game_board(size):
    problem = []
    row = []
    for i in range(size):
        for j in range(size):
            row.append(' ')
        problem.append(row)
        row = []
    return problem


def horizontal_line(size):
    return " ---" * size + " \n"


def vertical_lines(size, i, problem):
    row = """"""
    for j in range(size):
        row += "| "+problem[i][j]+" "
    row += "|\n"
    return row


def print_game_board(size, problem):
    board = """"""
    for i in range(size):
        board += horizontal_line(size)
        board += vertical_lines(size, i, problem)
    board += horizontal_line(size)
    return board


def is_legal(board, size, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True


def back_tracking(board, size, col):
    global iteration
    iteration += 1
    if col >= size:
        return True
    for i in range(size):
        if is_legal(board, size, i, col):
            board[i][col] = 'Q'
            if back_tracking(board, size, col + 1):
                return True
            board[i][col] = ' '
    return False


def solve_problem(size, problem):
    if not (back_tracking(problem, size, 0)):
        print("Problem doesn't has a solution")
    else:
        print(print_game_board(size, problem))
        print("Problem Solved")


if __name__ == "__main__":

    board_size = int(input("What size game board do You want? "))
    problem1 = create_game_board(board_size)
    solve_problem(board_size, problem1)
    print("{} iterations".format(iteration))















