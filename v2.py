from colorama import Fore
from enum import Enum

ONE_TO_NINE = [str(i+1) for i in range(9)]

threeSquareList = ""
for i in range(3):
    threeSquareList += f"\n{1+3*i},{2+3*i},{3+3*i}"
nineSquareList = [[f"{j+1}" for i in range(9)] for j in range(9)]
guide = "\nGuide:"
for k in range(3):
    guide += "\n"
    for j in range(3):
        guide += " / ".join([",".join(nineSquareList[i+k*3][0+j*3:3+j*3]) for i in range(3)]) + "\n"
guide += threeSquareList
guide += "\n\nType guide to show this guide\n"

isTurnofX = True
playerX = [[] for i in range(9)]
playerO = [[] for i in range(9)]
stop = False
freeBoard = True
lastBoard = 0
xColour = Fore.GREEN
oColour = Fore.CYAN
selectColour = Fore.YELLOW

class Board:
    def __init__(self, content) -> None:
        self.content = content

    def printContent(self):
        content = self.content
        for i in range(3):
            print(",".join(content[0+i*3:3+i*3]))

class BigBoard(Board):
    def printContent(self):
        output = "\nboard:"
        for k in range(3):
            output += "\n"
            for j in range(3):
                output += " / ".join([",".join(self.content[i+k*3].content[0+j*3:3+j*3]) for i in range(3)]) + "\n"
        print(output)

    def recolour(self, boardNumber=0, colour=Fore.WHITE):
        board = self.content[boardNumber].content
        if colour == Fore.WHITE:
            board = list(map(lambda x: x.replace(selectColour, "") , board))
            self.content[boardNumber].content = board
            return None
        # board = [colour + val + Fore.WHITE if (i+1)%3==0 else colour + val for i, val in enumerate(board)]
        board = list(map(lambda x: colour + x, board))
        board[2::3] = list(map(lambda x: x + Fore.WHITE, board[2::3]))
        #print(board)
        self.content[boardNumber].content = board

def validInput(text, board=0, box=False):
    global stop
    getInput = input(text)
    # print(getInput.__repr__())
    while 1:
        if getInput == "0":
            stop = True
            break
        if getInput == "guide":
            print(guide)
        if getInput not in ONE_TO_NINE:
            getInput = input(text)
            print("invalid chioce! " + "1-9 " if getInput in ONE_TO_NINE else "not 1-9 ")
            continue
        indexInput = int(getInput)-1
        targetBoxOccupied = indexInput in playerX[board] or indexInput in playerO[board] if box else indexInput in playerX or indexInput in playerO
        # print(f"x {playerX[board]}")
        # print(f"o {playerO[board]}")
        # print(f"input {indexInput}")
        # print(f"occupied {indexInput in playerX[board]}{indexInput in playerO[board]}{targetBoxOccupied}")
        if not targetBoxOccupied:
            break
        print("invalid chioce! " + "occupied " if targetBoxOccupied else "free ")
        
        getInput = input(text)
    return getInput
        
winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

bigBoard = BigBoard([Board(["_" for i in range(9)]) for _ in range(9)])
print(guide)
# bigBoard.printContent()

while not stop:
    print("")
    print(xColour + "X's turn -------------------" + Fore.WHITE) if isTurnofX else print(oColour + "O's turn -------------------" + Fore.WHITE)
    currentPlayer = playerX if isTurnofX else playerO
    bigBoard.recolour(lastBoard)
    #board chioce
    getBoard = int(validInput("Free board! choose board 1-9 >"))-1 if freeBoard else indexInput
    if stop: break
    bigBoard.recolour(getBoard, selectColour)
    bigBoard.printContent()
    #box chioce
    getInput = validInput("choose box 1-9 >", getBoard, True)
    if stop: break
    indexInput = int(getInput)-1
    bigBoard.content[getBoard].content[indexInput] = "x" if isTurnofX else "o"
    currentPlayer[getBoard].append(indexInput)
    # print(f"c {currentPlayer[getBoard]}")
    #check win
    for i in winConditions:
        if i[0] in currentPlayer[getBoard] and i[1] in currentPlayer[getBoard] and i[2] in currentPlayer[getBoard]:
            print(f"X captured {getBoard}") if isTurnofX else print(f"O captured {getBoard}")
            bigBoard.recolour(getBoard, xColour if isTurnofX else oColour)
            currentPlayer[getBoard] = getBoard
            if list(filter(lambda x: True if type(x) == int else False, currentPlayer)) in winConditions:
                print("\nX win!!\n") if isTurnofX else print("O win!!\n")
                stop = True
                break
            break
            
    #post chioce
    # print(f"x {playerX}")
    # print(f"o {playerO}")
    # print(f"input {indexInput}")
    lastBoard = getBoard
    targetBoardOccupied = indexInput in playerX or indexInput in playerO
    freeBoard = True if targetBoardOccupied else False
    isTurnofX = not isTurnofX
    # bigBoard.printContent()
    # print(f"{lastBoard} {targetBoardOccupied} {freeBoard} {indexInput}")

if stop: print("stopped")