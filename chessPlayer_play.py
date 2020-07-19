from chess import *
from chessPlayer import *

chessBoard = generateBoard()
whiteScore = 0
blackScore = 0

while True:
   #printBoard(chessBoard)
   while True:
      print("White Captured Pieces Are: ")
      #print(wCaptured)
      print("Black Captured Pieces Are: ")
      #print(bCaptured)
      print("")
      print("------WHITE TURN------\n")
      move = chessPlayer(chessBoard,20)[1]
      #print(move)
      tree = chessPlayer(chessBoard,10)[3]
      #tree.Print_DepthFirst()
      #print(chessPlayer(chessBoard,10)[2])
      score = makeMove(chessBoard, move[0],move[1])
      #whiteScore = score[1]
      #print("White Score is: " + str(score[1]))
      print("Moved " + str(move[0]) + " to " + str(move[1]))
      printBoard(chessBoard)
      input ("Please press any key to continue")
      break
   #printBoard(chessBoard)
   while True:
      print("------BLACK TURN------\n")
      blackStart = int(input("Which piece would you like to move?\n"))
      blackEnd = int(input("Where do you wish to move it to?\n"))
      move = chessPlayer(chessBoard,20)[1]
      tree = chessPlayer(chessBoard,10)[3]
      #print(chessPlayer(chessBoard,20)[3])
      #makeMove(chessBoard, blackStart,blackEnd)
      print("Moved " + str(blackStart) + " to " + str(blackEnd))
      printBoard(chessBoard)
      #input ("Please press any key to continue")
      #break
      if makeMove(chessBoard,blackStart,blackEnd)[0]==False:
        print("Please enter a valid input\n")
      else:
        break

   
