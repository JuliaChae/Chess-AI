from chessPlayer_tree import *
from random import *

def generateBoard():
   board=[]
   for row in range(0,64):
      board = board+[0]
   for r in range(0,8,7):
      board[r]=13
      board[56+r]=23     
   for r in range(1,7,5):
      board[r]=11
      board[56+r]=21     
   for r in range(2,6,3):
      board[r]=12
      board[56+r]=22       
   board[4] = 14
   board[60]= 24
   board [3] = 15
   board [59] = 25
   for r in range(8,16):
      board[r]=10
      board[40+r]=20
   return board
     
def printBoard(board):
   pBoard = []
   for elem in range(0,64):
      if board[elem] != 0 and board[elem]%10==0:
         if board[elem]>=20:
            pBoard=pBoard+['p']
         else:
            pBoard = pBoard + ['P']
      elif board[elem]%10==1:
         if board[elem]>=20:
            pBoard=pBoard+['n']
         else:
            pBoard = pBoard + ['N']
      elif board[elem]%10==2:
         if board[elem]>=20:
            pBoard=pBoard+['b']
         else:
            pBoard = pBoard + ['B']
      elif board[elem]%10==3:
         if board[elem]>=20:
            pBoard=pBoard+['r']
         else:
            pBoard = pBoard + ['R']
      elif board[elem]%10==4:
         if board[elem]>=20:
            pBoard=pBoard+['q']
         else:
            pBoard = pBoard + ['Q']
      elif board[elem]%10==5:
         if board[elem]>=20:
            pBoard=pBoard+['k']
         else:
            pBoard = pBoard + ['K']
      else:
         if (elem%2 == 0 and (elem//8)%2==0) or (elem%2 !=0 and (elem//8)%2 !=0):
            pBoard = pBoard + ['#']
         else:
            pBoard = pBoard + ['_']
   for row in range(56,-1,-8):
      print(str(pBoard[row+7])+" "+ str(pBoard[row+6])+" " +str(pBoard[row+5])+" "+str(pBoard[row+4])+" "+str(pBoard[row+3])+" "+str(pBoard[row+2])+" "+str(pBoard[row+1])+" "+str(pBoard[row]))
   return True 

def GetPlayerPositions(board,player):
   positions = []
   if player == 10:
      for elem in range(0,64):
         if board[elem]>= 10 and board[elem]<20:
            positions = positions + [elem]
   elif player == 20:
      for elem in range(0,64):
         if board[elem] >= 20:
            positions = positions + [elem]
   else:
      return False
   return positions

def GetPieceLegalMoves(board, position):
   if board[position]!=0 and board[position]%10==0:
      return getPawnMoves(board, position)
   elif board[position]%10==1:
      return getKnightMoves(board, position)
   elif board[position]%10==2:
      return getBishopMoves(board,position)
   elif board[position]%10==3:         
      return getRookMoves(board, position)
   elif board[position]%10==4:
      return getQueenMoves(board,position)
   elif board[position]%10==5:
      return getKingMoves(board, position)
   else:
      return []
      
def getPawnMoves(board,position):
   moves = []
   forward = 0
   if board[position]>=20:
      forward = -8
   else:
      forward = 8
   if (position+forward)<64 and (position+forward)>=0: 
      if board[position+forward] == 0:
         moves = moves + [position+forward] 
      if (position+forward)<63 and (position)%8!=7:
         if isEnemy(board[position], board[position+forward+1])==True:
            moves = moves + [position+forward+1]
      if (position+forward)>0 and (position)%8!=0:
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
            if captured >= 20:
               captured = returnPieceValue(captured,board[end], end,20)
            elif captured == 0:
               if start >= 20:
                  captured = returnPieceValue (captured,board[end], end,10)
               else:
                  captured = returnPieceValue (captured,board[end], end,20)
            else:
               captured = returnPieceValue(captured,board[end], end, 10) 
            return [True,captured]
   return [False,captured]


def alphabeta(tree,depth,alpha,beta,maxP):
   index =0
   if depth == 0 or tree.store[1]==[]:
      return tree.store[0][0]
   if maxP == True:
      for x in range(0,len(tree.store[1])):
         alpha = maxmin(alpha, alphabeta(tree.store[1][x], depth-1,alpha,beta,False),True)
         if alpha > beta:
            break;
      return alpha
   elif maxP == False:
      for x in range(0,len(tree.store[1])):
         beta = maxmin(beta,alphabeta(tree.store[1][x], depth-1,alpha,beta,True),False)
         if alpha > beta:
            break
      return beta

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
   if catcher%10 == 0:
      point = float((factor*(piece%10))*10) + (factor*pawnOffset[index])
   elif catcher%10 == 1:
      point = float((factor*(piece%10))*10) + (factor*knightOffset[index])
   elif catcher%10 == 2:
      point = float((factor*(piece%10))*10) + (factor*bishopOffset[index])
   elif catcher%10 == 3:
      point = float((factor*(piece%10))*10) + (factor*rookOffset[index])
   elif catcher%10 == 4:
      point = float((factor*(piece%10))*10) + (factor*queenOffset[index])
   elif catcher%10 == 5: 
      point = float((factor*(piece%10))*1000) + (factor*kingOffset[index])
   return point 

def alphabeta_tree(node,depth,alpha,beta,maxP):
   abTree = tree([0.0])
   for x in node.store[1]:
      succ = alphabeta(x,depth-1,alpha,beta,maxP)
      abTree.AddSuccessor(tree([succ]))
   return abTree 

def maxmin(a,b,maximum):
   if maximum==True:
      if a>=b:
         return a
      else:
         return b
   else:
      if a<=b:
         return a
      else:
         return b

def generatePositionTree(intree,board,team,depth):
   tboard = list(board)
   if team ==20:
      low = 20
      high = 30
   else:
      low = 10
      high = 20
   for index in range(0,64):
      if board[index]>=low and board[index]<high:
         for i in GetPieceLegalMoves(board,index):
            status = makeMove(tboard,index,i)
            if status[0]!=False:
               succ = tree([intree.store[0][0]+status[1],tboard])
               intree.AddSuccessor(succ)
            tboard = list(board)
   return intree

def generateGameTree(node,board,team,depth):
   if depth == 0:
      return 0
   else:
      rtree=generatePositionTree(node,board,team,depth)
      for x in rtree.store[1]:
         if team == 20: 
            generateGameTree(x,x.store[0][1],10,depth-1)
         else:
            generateGameTree(x,x.store[0][1],20,depth-1)
   return rtree

def chessPlayer(board,player):
   depth =2
   white = True
   equivalent = []
   score = []
   a = tree([0.0])
   gtree=generateGameTree(a,board,player,depth)
   if player == 20:
      white = False
   ab= alphabeta_tree(gtree,depth,-1000000,100000,not(white))
   maximum = ab.store[1][0].store[0][0]
   for x in ab.store[1]:
      score = score + [x.store[0][0]]
      if player == 10:
         if x.store[0][0]>maximum:
            maximum = x.store[0][0]
      else:
         if x.store[0][0]<maximum:
            maximum = x.store[0][0]
   for x in range(0,len(ab.store[1])):
      if ab.store[1][x].store[0][0] == maximum:
         equivalent = equivalent + [x] 
   candidateMoves = possibleMoves(board,player,score)
   x= randint(0,len(equivalent)-1)
   move = candidateMoves[equivalent[x]][0]
   return [True, move, candidateMoves, gtree.Get_LevelOrder()]

def possibleMoves(board,team,score):
   moves = []
   tboard = list(board)
   count = 0
   if team == 20:
      low = 20
      high = 30
   else:
      low = 10
      high = 20
   for index in range(0,64):
      if board[index]>=low and board[index]<high:
         for i in GetPieceLegalMoves(board,index):
            status = makeMove(tboard,index,i)
            if status[0]!=False:
               moves = moves + [[[index, i],score[count]]] 
               count = count+1
            tboard = list(board)
   return moves  
