class Step:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def is_valid(x, y, M, N):
    return 1 <= x <= M and 1 <= y <= N


def possible_knight_moves(x, y, M, N):
    moves = [
        (x + 2, y + 1),
        (x + 2, y - 1),
        (x - 2, y + 1),
        (x - 2, y - 1),
        (x + 1, y + 2),
        (x + 1, y - 2),
        (x - 1, y + 2),
        (x - 1, y - 2),
    ]

    valid_moves = [(nx, ny) for nx, ny in moves if is_valid(nx, ny, M, N)]
    return valid_moves


M, N = map(int, input("Enter the board dimensions (M N): ").split())
x, y = map(int, input("Enter the knight's position (x y): ").split())

moves = possible_knight_moves(x, y, M, N)