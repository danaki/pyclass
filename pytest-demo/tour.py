moves = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]

def to_chess_notation(x, y):
    return 'abcdefgh'[x] + str(y + 1)

def from_chess_notation(s):
    return 'abcdefgh'.index(s[0]), int(s[1]) - 1

def chess_notation_to_list(s):
    return [from_chess_notation(x) for x in s.split(' ')]

def is_board_hit(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

def is_valid_move(fr, to):
    return (to[0] - fr[0], to[1] - fr[1]) in moves and is_board_hit(to[0], to[1])

def is_valid_solution(solution):
    board = [[0 for x in range(8)] for y in range(8)]

    path = chess_notation_to_list(solution)
    turn = 0

    while True:
        x, y = path.pop(0)

        if not is_board_hit(x, y) or board[x][y] > 0:
            break

        turn += 1
        board[x][y] = turn

        if turn == 64:
            return True

    return False
