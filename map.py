from __future__ import print_function
from level_types import *

class Map:


    def fill_matrix(selfl,matrix):
        matrix[Positions.AGENT_x][Positions.AGENT_y] = BlockType.AGENT
        matrix[0][5] = BlockType.BRICK
        matrix[1][5] = BlockType.BRICK
        matrix[2][6] = BlockType.BRICK
        matrix[4][5] = BlockType.BRICK
        matrix[2][6] = BlockType.BRICK
        matrix[2][3] = BlockType.BRICK
        matrix[2][4] = BlockType.FAST
        matrix[Positions.OPONENT_x][Positions.OPONENT_y] = BlockType.OPPONENT

        return

    def paint_map(self,dimension,matrix):

        x = dimension
        y = dimension
        even = False
        offset = False
        count = 0

        for i in range(2*x):
            for j in range(y):
                if(even):
                    print('\ /', end="")
                else:
                    print("/ \\", end="")
            count+=1
            print("")

            if(count == 2):
                offset= ~offset
                count=0

            if(~even):
                if (offset):
                    print(" ", end="")
                for j in range(y):
                    print("|",end="")
                    print(matrix[i/2][j], end="")
                    print("|", end="")
                print("")

            if(offset):
                print(" ", end="")



            even = ~even

        return







