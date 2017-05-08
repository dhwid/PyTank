import time
from level_types import *
from map import *

class AI:


    x = 0
    y = 0

    def oponent(self,matrix,dimension,changes,history):
        #map = Map()
        if(Positions.OPONENT_exist):
        #if(time.clock() - Positions.OPONENT_time> 0.5):
            if(Positions.OPONENT_direction_right):
                self.y = Positions.OPONENT_y + 1
                if (self.y < dimension):
                    if (matrix[Positions.OPONENT_x][self.y] == 0):
                        matrix[Positions.OPONENT_x][Positions.OPONENT_y] = 0
                        matrix[Positions.OPONENT_x][self.y] = 2
                        history.addOponent("1")

                        changes[Positions.OPONENT_x][Positions.OPONENT_y] = 1
                        changes[Positions.OPONENT_x][self.y] = 1

                        Positions.OPONENT_y = self.y
                        #map.paint_map(dimension, matrix)
                    else: Positions.OPONENT_direction_right=False
                else:
                    Positions.OPONENT_direction_right=False
            else:
                self.y = Positions.OPONENT_y - 1
                if (self.y >= 0):
                    if (matrix[Positions.OPONENT_x][self.y] == 0):
                        matrix[Positions.OPONENT_x][Positions.OPONENT_y] = 0
                        matrix[Positions.OPONENT_x][self.y] = 2
                        history.addOponent("2")

                        changes[Positions.OPONENT_x][Positions.OPONENT_y] = 1
                        changes[Positions.OPONENT_x][self.y] = 1

                        Positions.OPONENT_y = self.y
                        #map.paint_map(dimension,matrix)
                    else:
                        Positions.OPONENT_direction_right = True
                else:
                    Positions.OPONENT_direction_right=True


            Positions.OPONENT_time = time.clock()
