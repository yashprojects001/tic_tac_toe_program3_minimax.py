# STEP 1: Board Representation
# 0 = empty, 1 = Human (X), 2 = AI (O)

board = [0,0,0,
         0,0,0,
         0,0,0]

# STEP 2: Display Board

def print_board():
    symbols = [' ', 'X', 'O']
    print()
    for i in range(0, 9, 3):
        print(" ", symbols[board[i]], "|", symbols[board[i+1]], "|", symbols[board[i+2]])
        if i < 6:
            print(" ---+---+---")
    print()

# STEP 3: Winning Positions

win_positions = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

# STEP 4: Check Winner

def check_winner(player):
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return 0 not in board

# STEP 5: Evaluation Function

def evaluate():
    if check_winner(2):
        return 1
    if check_winner(1):
        return -1
    return 0

# STEP 6: Minimax Algorithm

def minimax(is_ai_turn):
    score = evaluate()

    if score != 0:
        return score
    if is_draw():
        return 0

    if is_ai_turn:
        best = -1000
        for i in range(9):
            if board[i] == 0:
                board[i] = 2
                value = minimax(False)
                board[i] = 0
                best = max(best, value)
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                value = minimax(True)
                board[i] = 0
                best = min(best, value)
        return best

# STEP 7: Best Move Finder

def best_move():
    best_score = -1000
    move = -1

    for i in range(9):
        if board[i] == 0:
            board[i] = 2
            score = minimax(False)
            board[i] = 0

            if score > best_score:
                best_score = score
                move = i

    return move

# STEP 8: Human Move

def human_move():
    while True:
        pos = int(input("Enter position (1-9): ")) - 1
        if 0 <= pos <= 8 and board[pos] == 0:
            return pos
        print("Invalid move. Try again.")

# STEP 9: Main Game Loop

while True:
    print_board()

    board[human_move()] = 1

    if check_winner(1):
        print_board()
        print("🎉 You win!")
        break

    if is_draw():
        print("It's a draw!")
        break

    ai = best_move()
    board[ai] = 2

    if check_winner(2):
        print_board()
        print("🤖 AI wins!")
        break
