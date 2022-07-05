import math
import random


import numpy as np
class Maze:
   def __init__(self):
      self.n = 0
      self.maze = np.zeros
      self.sets = np.zeros
   def GenerateMaze(self,n):
      #Initialize Grid
      self.maze = np.zeros([n,n])

      count = 0
      iterations = 15
      for z in range(0, iterations, 1):

         whitespacex = []
         whitespacey = []

         for x in range (1,n-1,1):
            for y in range (1,n-1,1):
               if(count == 0):
                  rand = random.randint(0,10)
                  if(rand != 0):
                     rand = 0
                  else:
                     rand = -1
                  self.maze[x,y] = rand


               if (self.maze[x, y] == -1):
                  whitespacex.append(x)
                  whitespacey.append(y)
         for i in range (0, len(whitespacey), 1):
            print("i")
            x = whitespacex[i]
            y = whitespacey[i]
            self.maze[x, y] = -1
            if(random.randint(0,1) == 0):
               for j in range (-4,4 , 1):
                  x = x + j
                  self.maze[x, y] = -1

            if (random.randint(0, 1) == 1):
               for j in range (-4, 4, 1):
                  y = y + j
                  self.maze[x, y] = -1


      #Generate Borders
      for x in range(0,n,1):
         self.maze[x, n-1] = 0
      for x in range(0,n,1):
         self.maze[x, 0] = 0
      for x in range(0,n,1):
         self.maze[0, x] = 0
      for x in range(0,n,1):
         self.maze[n-1, x] = 0

      for x in range(1, n - 1, 1):
         for y in range(1, n - 1, 1):
            if (self.maze[x, y] == 0):
               count = 0
               if (self.maze[x - 1, y] == -1):
                  count += 1
               if (self.maze[x + 1, y] == -1):
                  count += 1
               if (self.maze[x, y - 1] == -1):
                  count += 1
               if (self.maze[x, y + 1] == -1):
                  count += 1
               if (self.maze[x - 1, y - 1] == -1):
                  count += 1
               if (self.maze[x + 1, y + 1] == -1):
                  count += 1
               if (self.maze[x - 1, y + 1] == -1):
                  count += 1
               if (self.maze[x + 1, y - 1] == -1):
                  count += 1
               if (count > 6):
                  self.maze[x, y] = -1