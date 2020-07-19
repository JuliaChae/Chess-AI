from chessPlayer_queue import *

class tree:
   def __init__(self,x):
      self.store = [x,[]]
      self.levelOrder = []

   def AddSuccessor (self,x):
      self.store[1] = self.store[1]+[x]
      return True

   def getSuccessors (self):
      return self.store[1]

   def Print_DepthFirst_2(self,indent):
      print(indent +str(self.store[0][0])) 
      for x in self.store[1]:
         x.Print_DepthFirst_2(indent+"   ")
      return True

   def Print_DepthFirst(self):
      self.Print_DepthFirst_2("")
      return True 

   def Get_LevelOrder(self):
      x =Queue()
      x.enqueue(self)
      accum = []
      while x.empty() == False:
         r=x.dequeue()
         accum = accum + [r.store[0][0]]
         for i in r.store[1]:
            x.enqueue(i)
      return accum


