from chessPlayer_tree import *
from chess import *

def alphabeta(tree,depth,alpha,beta,maxP):
   #print(tree.store[0])
   index =0
   rlist = []
   if depth == 0:
   #   print("hi") 
      return [tree.store[0],0]
   if maxP == True:
      for x in range(0,len(tree.store[1])):
         alpha = maxmin(alpha, alphabeta(tree.store[1][x], depth-1,alpha,beta,False)[0],True)
         rlist = rlist + [alpha[0]]
         if alpha[0] > beta[0]:
            index = x
      print("returning alpha "  + str(alpha[0]))
      return [alpha,x,rlist]
   elif maxP == False:
      for x in range(0,len(tree.store[1])):
         beta = maxmin(beta,alphabeta(tree.store[1][x], depth-1,alpha,beta,True)[0],False)
         rlist = rlist + [beta[0]]
         if alpha[0] > beta[0]:
            index = x
      print("returning beta "+ str(beta[0]))
      return [beta,x,rlist]

def maxmin(a,b,maximum):
   if maximum==True:
      if a[0]>=b[0]:
         return a
      else:
         return b
   else:
      if a[0]<=b[0]:
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
      if board[index]>low and board[index]<high:
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
   depth = 3
   white = True
   a = tree([0.0])
   gtree=generateGameTree(a,board,player,depth)
   gtree.Print_DepthFirst()
   if player == 20:
      white = False
   ab= alphabeta(gtree,depth,[-1000000.0],[100000.0],white)
   print(ab[2])
   candidateMoves = possibleMoves(board,player,ab[2])
   move = candidateMoves[ab[1]][0]
   return [True, move, candidateMoves,gtree]


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
      if board[index]>low and board[index]<high:
         for i in GetPieceLegalMoves(board,index):
            status = makeMove(tboard,index,i)
            if status[0]!=False:
               moves = moves + [[[index, i],score[count]]] 
               count = count+1
            tboard = list(board)
   print(moves)
   return moves   
