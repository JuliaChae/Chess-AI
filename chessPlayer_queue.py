class Queue:
   def __init__(self):
      self.queue= []
   
   def enqueue(self, x_in):
      self.queue = self.queue+ [x_in]
      return True
   
   def dequeue(self):
      rval = self.queue[0]
      self.queue  = self.queue[1:len(self.queue)]
      return rval
  
   def empty(self):
      if len(self.queue)==0:
         return True
      else:
         return False 
