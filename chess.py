def generateBoard():
   board=[]
   for row in range(0,64):
      board = board+[0]
   for r in range(0,8,7):
      board[r]=15
      board[56+r]=25     
   for r in range(1,7,5):
      board[r]=13
      board[56+r]=23     
   for r in range(2,6,3):
      board[r]=14
      board[56+r]=24       
   board[4] = 18
   board[60]= 28
   board [3] = 19
   board [59] = 29
 #  board[36] = 28
 #  board[27]=11
   for r in range(8,16):
      board[r]=11
      board[40+r]=21
   return board
     
def printBoard(board):
   pBoard = []
   for elem in range(0,64):
      if board[elem]%10==1:
         if board[elem]>20:
            pBoard=pBoard+['p']
         else:
            pBoard = pBoard + ['P']
      elif board[elem]%10==3:
         if board[elem]>20:
            pBoard=pBoard+['n']
         else:
            pBoard = pBoard + ['N']
      elif board[elem]%10==4:
         if board[elem]>20:
            pBoard=pBoard+['b']
         else:
            pBoard = pBoard + ['B']
      elif board[elem]%10==5:
         if board[elem]>20:
            pBoard=pBoard+['r']
         else:
            pBoard = pBoard + ['R']
      elif board[elem]%10==8:
         if board[elem]>20:
            pBoard=pBoard+['q']
         else:
            pBoard = pBoard + ['Q']
      elif board[elem]%10==9:
         if board[elem]>20:
            pBoard=pBoard+['k']
         else:
            pBoard = pBoard + ['K']
      else:
         if (elem%2 == 0 and (elem//8)%2==0) or (elem%2 !=0 and (elem//8)%2 !=0):
            pBoard = pBoard + ['#']
         else:
            pBoard = pBoard + ['_']
   for row in range(56,-1,-8):
      #print(str(board[row])+" "+ str(board[row+1])+" " +str(board[row+2])+" "+str(board[row+3])+" "+str(board[row+4])+" "+str(board[row+5])+" "+str(board[row+6])+" "+str(board[row+7]))
      print(str(pBoard[row+7])+" "+ str(pBoard[row+6])+" " +str(pBoard[row+5])+" "+str(pBoard[row+4])+" "+str(pBoard[row+3])+" "+str(pBoard[row+2])+" "+str(pBoard[row+1])+" "+str(pBoard[row]))
   return True 

def GetPlayerPositions(board,player):
   positions = []
   if player == 10:
      for elem in range(0,64):
         if board[elem]> 10 and board[elem]<20:
            positions = positions + [elem]
   elif player == 20:
      for elem in range(0,64):
         if board[elem] > 20:
            positions = positions + [elem]
   else:
      return False
   return positions

def GetPieceLegalMoves(board, position):
   if board[position]%10==1:
      return getPawnMoves(board, position)
   elif board[position]%10==3:
      return getKnightMoves(board, position)
   elif board[position]%10==4:
      return getBishopMoves(board,position)
   elif board[position]%10==5:         
      return getRookMoves(board, position)
   elif board[position]%10==8:
      return getQueenMoves(board,position)
   elif board[position]%10==9:
      return getKingMoves(board, position)
   else:
      return []
      
def getPawnMoves(board,position):
   moves = []
   forward = 0
   if board[position]>20:
      forward = -8
   else:
      forward = 8
   if (position+forward)<64 and (position+forward)>=0: 
      if board[position+forward] == 0:
         moves = moves + [position+forward] 
      if (position+forward)<63:
         if isEnemy(board[position], board[position+forward+1])==True:
            moves = moves + [position+forward+1]
      if (position+forward)>0:
         if isEnemy(board[position],board[position+forward-1])==True:
            moves = moves + [position+forward-1]
   return moves

def getKnightMoves(board,position):
   moves = []
   positions = [-10,6,-17,15,-15,17,-6,10]
   if position%8==0:
      positions = positions[4:]
   elif position%8 ==1:
      positions = positions[2:]
   elif position%8==6:
      positions = positions[0:6]
   elif position%8==7:
      positions = positions[0:4]
   for x in positions:
      if position+x <64 and position+x>=0:
         if board[position+x]==0 or isEnemy(board[position],board[position+x])==True:
            moves = moves + [position+x]
   return moves

def getBishopMoves(board,position):
   moves = []
   diagonals = [9,-9,7,-7]
   bounds = [7,0,0,7]
   for x in range(0,4):
      pos = position
      while True:
         if pos <64 and pos >=0:
            if pos%8 == bounds[x] or isEnemy(board[position],board[pos])==True:
               if pos%8 == bounds[x] and isEnemy(board[position],board[pos])==False and board[pos]!=0:
                  break
               if pos!= position:
                  moves = moves + [pos]
               #   print("1")
                  break
               else:
                  break 
            elif board[pos] !=0 and isEnemy(board[position],board[pos])==False:
               if pos!=position:
                  break
            else: 
               moves = moves + [pos]
         else:
               break
         pos = pos + diagonals[x]
   return moves
          
def getRookMoves(board, position):
   moves = []
   shift = [1,-1,8,-8]
   bounds = [7,0,-1,-1]
   for x in range(0,4):
      pos = position
      while True:
         if pos<64 and pos >= 0:
            if pos%8 == bounds[x] or isEnemy(board[position],board[pos])==True:
               if pos%8 == bounds[x] and isEnemy(board[position],board[pos])==False and board[pos]!=0:
                  break
               if pos != position:
                  moves = moves + [pos]
                  break
               else: 
                  break 
            elif board[pos] !=0 and isEnemy(board[position],board[pos])==False:
               if pos!=position:
                  break
            else:
               moves = moves + [pos]
         else:
               break
         pos = pos + shift[x]
   return moves    

def getQueenMoves(board,position):
   moves = getBishopMoves(board,position) + getRookMoves(board,position)
   return moves

def getKingMoves(board,position):
   moves=[]
   shift = [1,-1,8,-8,9,-9,7,-7]
   bounds = [7,0,-1,-1,7,0,0,7]
   for x in range(0,8):
      pos = position + shift[x]
      if pos<64 and pos >= 0:
         if position%8 != bounds[x]:
            if board[pos]==0 or isEnemy(board[position],board[pos])==True:
               moves = moves + [pos]
   return moves    

def IsPositionUnderThreat(board,position,player):
   for elem in range(0,64):
      if isEnemy(board[elem],player)==False:
         if GetPieceLegalMoves(board,elem) != False:
            for x in GetPieceLegalMoves(board,elem):
               if position == x:
                  return True   
   return False

def isEnemy(piece, check):
   if piece >=20:
      if check < 20 and check >=10:
         return True
      else:
         return False
   else:
      if check >= 20:
         return True
      else:
         return False

def makeMove(board, start, end):
   captured =0;
   if GetPieceLegalMoves(board,start)!=False:
      for x in GetPieceLegalMoves(board,start):
         if x == end:
            if board[end]!=0:
               captured = board[end]
            board[end] = board[start]
            board[start]=0
            #print("Got here")
            if captured > 20:
               captured = returnPieceValue(captured,board[end], end,20)
            elif captured == 0:
               if start > 20:
                  captured = returnPieceValue (captured,board[end], end,10)
               else:
                  captured = returnPieceValue (captured,board[end], end,20)
            else:
               captured = returnPieceValue(captured,board[end], end, 10) 
            return [True,captured]
   return [False,captured]

def returnPieceValue(piece, catcher, index, team):
   factor = 1.0
   point = 0;
   pawnOffset = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0, 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0, 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5, 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0, 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5, 0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
   knightOffset = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0, -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0, -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0, -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0, -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0, -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0, -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0, -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
   bishopOffset = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,  -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,  -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,  -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0, -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,  -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,  -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0, -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
   rookOffset = [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,  -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
   queenOffset = [ 2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,  -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0, -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0, -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5, 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,  -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0, -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0, -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
   kingOffset = [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, .0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,  -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0, 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0, 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0] 
   if catcher > 10 and catcher <20:
      index = 63-index
   else:
      factor = -1
   #print(index)
   if catcher%10 == 1:
      point = float((factor*(piece%10))*10) + (factor*pawnOffset[index])
   elif catcher%10 == 3:
      point = float((factor*(piece%10))*10) + (factor*knightOffset[index])
   elif catcher%10 == 4:
      point = float((factor*(piece%10))*10) + (factor*bishopOffset[index])
   elif catcher%10 == 5:
      point = float((factor*(piece%10))*10) + (factor*rookOffset[index])
   elif catcher%10 == 8:
      point = float((factor*(piece%10))*10) + (factor*queenOffset[index])
   elif catcher%10 == 9: 
      point = float((factor*(piece%10))*100) + (factor*kingOffset[index])
   return point 
#print(generateBoard())

def main(): 
   chessBoard = generateBoard()
   print(makeMove(chessBoard,27,36))
   printBoard(chessBoard)


#main()

