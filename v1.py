playerX = []
playerO = []
turnX = True
board = ["_" for _ in range(9)]
boardInstructions = ""
for i in range(3):
    boardInstructions += f"{1+3*i},{2+3*i},{3+3*i}\n"
getInput = ""
winConditions = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"],
    ["1","4","7"],
    ["2","5","8"],
    ["3","6","9"],
    ["1","5","9"],
    ["3","5","7"]
]

stop = False

print(boardInstructions)
    
while not stop:
    print("\nX's turn") if turnX else print("\nO's turn")
    currentPlayer = playerX if turnX else playerO
    print("board: \n")
    for i in range(3):
        print(f"{board[0+3*i]},{board[1+3*i]},{board[2+3*i]}")
    getInput = input("\n> ")
    while 1:
        if getInput in str([i+1 for i in range(9)]) and getInput not in playerX and getInput not in playerO and getInput.isdecimal():
            break
        if getInput == "0":
            stop = True
            break
        if getInput == "instr":
            print(boardInstructions)
        getInput = input("\n> ")
    board[int(getInput)-1] = "x" if turnX else "o"
    currentPlayer.append(getInput)
    # print(playerX)
    # print(playerO)
    # if len(currentPlayer) < 3:
    #     turnX = not turnX
    #     continue
    for i in winConditions:
        if i[0] in currentPlayer and i[1] in currentPlayer and i[2] in currentPlayer:
            print("\nX win!!\n") if turnX else print("O win!!\n")
            stop = True
            break
    if "_" not in board and not stop:
        print("\ndraw!!\n")
        stop = True
    turnX = not turnX

for i in range(3):
    print(f"{board[0+3*i]},{board[1+3*i]},{board[2+3*i]}")


# for i in range(9):
#     board.append([i for i in range(9)])
