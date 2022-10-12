import random
board = [' ' for i in range(10)]
def insertLetter(letter, pos):
  board[pos] = letter
def printBoard(board):
  print("   |   |   ")
  print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
  print("   |   |   ")
  print(" ---------")
  print("   |   |   ")
  print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
  print("   |   |   ")
  print(" ---------")
  print("   |   |   ")
  print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
  print("   |   |   ")
def isFreeSpace(pos):
  return board[pos] == ' '
def isBoardFull(board):
  if board.count(' ') > 1:
    return False
  else:
    return True
def isWinner(board, letter):
  return (board[1] == letter and board[2] == letter and board[3] == letter
          or board[4] == letter and board[5] == letter and board[6] == letter
          or board[7] == letter and board[8] == letter and board[9] == letter
          or board[1] == letter and board[4] == letter and board[7] == letter
          or board[2] == letter and board[5] == letter and board[8] == letter
          or board[3] == letter and board[6] == letter and board[9] == letter
          or board[1] == letter and board[5] == letter and board[9] == letter
          or board[3] == letter and board[5] == letter and board[7] == letter)


def playerMove():
  run = True
  while run:
    move = input("Enter the position of X between 1 to 9")
    try:
      move = int(move)
      if move > 0 and move < 10:
        if isFreeSpace(move):
          run = False
          insertLetter("X", move)
          printBoard(board)
        else:
          print("The position is already occupied")
      else:
        print("Enter a number between 1-9")
    except:
      print("Enter an integer")


def computerMove():
  possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0 ]

  move = 0

  for let in ['X' , '0']:
    for i in possibleMoves:
      boardcopy = board[:]
      boardcopy[i] = let
      if isWinner(boardcopy,let):
        move = i
        return move

  cornersOpen = []
  for i in possibleMoves:
    if i in  [1,3,7,9]:
      cornersOpen.append(i)
        
  if len(cornersOpen) > 0:
    move = selectRandom(cornersOpen)
    return move

  if 5 in possibleMoves:
    move = 5 
    return move
  
  edgesOpen = []
  for i in possibleMoves:
    if i in [2,4,6,8]:
      edgesOpen.append(i)

  if len(edgesOpen) > 0:
    move = selectRandom(edgesOpen)
    return move
  def selectRandom(li):
    ln = len(li)
    r = random.randRange(0,ln)
    return li[r]
  

computerMove()