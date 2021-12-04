filename = "input.txt"
f = open(filename).read().strip().split("\n\n")
numbers = list(map(int, f[0].split(",")))
boards = [[list(map(int, row.split())) 
    for row in board.split("\n")] for board in f[1:]]

called_set = set()
def board_check():
    for number in numbers:
        called_set.add(number)
        for i, board in enumerate(boards):
            
            for r in range(5): # check every row
                f = True
                for i in range(5): # check horizontal win (row same, col diff)
                    if board[r][i] not in called_set: f = False
                if f: return (board, number)

            for c in range(5):
                f = True
                for i in range(5): # check veritcal win (row diff, col same)
                    if board[i][c] not in called_set: f = False
                if f: return (board, number)

def board_check_p2():
    no_wins = set(range(len(boards)))
    for number in numbers:
        called_set.add(number)
        for num_board, board in enumerate(boards):
            if num_board not in no_wins: continue

            for r in range(5): # check every row
                f = True
                for i in range(5): # check horizontal win (row same, col diff)
                    if board[r][i] not in called_set: f = False

                if f and len(no_wins) == 0: return (board, number)
                elif f: no_wins.discard(num_board)

            for c in range(5):
                f = True
                for i in range(5): # check veritcal win (row diff, col same)
                    if board[i][c] not in called_set: f = False

                if f and len(no_wins) == 0: return (board, number)
                elif f: no_wins.discard(num_board)

for soln in [board_check, board_check_p2]:
    called_set, s = set(), 0
    board, numb = soln()
    for i in range(25):
        if board[i//5][i%5] not in called_set: s += board[i//5][i%5]
    print(s * numb)
