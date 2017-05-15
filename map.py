from __future__ import print_function
from level_types import *

class Map:



    def fill_matrix(selfl,matrix):
        matrix[Positions.AGENT_x][Positions.AGENT_y] = BlockType.AGENT
        matrix[0][5] = BlockType.BRICK
        matrix[1][5] = BlockType.BRICK
        matrix[2][6] = BlockType.BRICK
        matrix[5][5] = BlockType.BRICK
        matrix[2][6] = BlockType.BRICK
        matrix[2][4] = BlockType.FAST
        matrix[10][6] = BlockType.BRICK
        matrix[11][6] = BlockType.BRICK
        matrix[0][0] = BlockType.BRICK
        matrix[0][1] = BlockType.BRICK
        matrix[1][1] = BlockType.BRICK
        matrix[1][2] = BlockType.FAST
        matrix[2][7] = BlockType.BRICK
        matrix[2][8] = BlockType.BRICK
        matrix[3][8] = BlockType.BRICK
        matrix[4][0] = BlockType.BRICK
        matrix[4][1] = BlockType.BRICK
        matrix[5][1] = BlockType.BRICK
        matrix[2][2] = BlockType.FAST
        matrix[1][10] = BlockType.BRICK
        matrix[3][11] = BlockType.FAST
        matrix[2][11] = BlockType.FAST
        matrix[0][10] = BlockType.BRICK
        matrix[5][4] = BlockType.FAST
        matrix[7][0] = BlockType.FAST
        matrix[8][1] = BlockType.BRICK
        matrix[9][1] = BlockType.BRICK
        matrix[10][1] = BlockType.FAST
        matrix[4][11] = BlockType.BRICK
        matrix[4][8] = BlockType.BRICK
        matrix[5][8] = BlockType.BRICK
        matrix[0][19] = BlockType.FAST
        matrix[1][18] = BlockType.FAST
        matrix[2][18] = BlockType.BRICK
        matrix[2][17] = BlockType.BRICK
        matrix[2][16] = BlockType.FAST
        matrix[2][15] = BlockType.FAST
        matrix[2][14] = BlockType.BRICK
        matrix[3][14] = BlockType.BRICK
        matrix[4][14] = BlockType.FAST
        matrix[5][14] = BlockType.BRICK
        matrix[5][11] = BlockType.FAST
        matrix[7][15] = BlockType.BRICK
        matrix[8][16] = BlockType.BRICK
        matrix[9][16] = BlockType.BRICK
        matrix[10][17] = BlockType.FAST
        matrix[5][17] = BlockType.BRICK
        matrix[7][18] = BlockType.FAST
        matrix[8][19] = BlockType.BRICK
        matrix[7][3] = BlockType.BRICK
        matrix[8][4] = BlockType.BRICK
        matrix[9][4] = BlockType.FAST
        matrix[9][5] = BlockType.FAST
        matrix[8][8] = BlockType.BRICK
        matrix[8][9] = BlockType.BRICK
        matrix[8][10] = BlockType.BRICK
        matrix[8][11] = BlockType.FAST
        matrix[8][12] = BlockType.FAST
        matrix[8][13] = BlockType.BRICK
        matrix[9][13] = BlockType.FAST
        matrix[18][5] = BlockType.BRICK
        matrix[19][5] = BlockType.BRICK
        matrix[11][7] = BlockType.BRICK
        matrix[11][8] = BlockType.BRICK
        matrix[11][9] = BlockType.FAST
        matrix[11][10] = BlockType.FAST
        matrix[11][11] = BlockType.FAST
        matrix[11][14] = BlockType.BRICK
        matrix[12][14] = BlockType.BRICK
        matrix[13][13] = BlockType.FAST
        matrix[13][0] = BlockType.BRICK
        matrix[13][1] = BlockType.BRICK
        matrix[12][2] = BlockType.BRICK
        matrix[12][4] = BlockType.FAST
        matrix[13][4] = BlockType.BRICK
        matrix[14][4] = BlockType.BRICK
        matrix[15][3] = BlockType.BRICK
        matrix[16][3] = BlockType.FAST
        matrix[17][2] = BlockType.FAST
        matrix[14][13] = BlockType.FAST
        matrix[14][12] = BlockType.BRICK
        matrix[14][11] = BlockType.BRICK
        matrix[14][10] = BlockType.BRICK
        matrix[14][9] = BlockType.BRICK
        matrix[14][8] = BlockType.FAST
        matrix[14][7] = BlockType.FAST
        matrix[18][0] = BlockType.FAST
        matrix[19][0] = BlockType.FAST
        matrix[15][13] = BlockType.FAST
        matrix[16][14] = BlockType.BRICK
        matrix[17][14] = BlockType.BRICK
        matrix[1][7] = BlockType.BRICK
        matrix[18][15] = BlockType.FAST
        matrix[19][15] = BlockType.FAST
        matrix[17][7] = BlockType.FAST
        matrix[17][8] = BlockType.BRICK
        matrix[17][9] = BlockType.BRICK
        matrix[17][10] = BlockType.BRICK
        matrix[17][11] = BlockType.FAST
        matrix[18][8] = BlockType.BRICK
        matrix[19][8] = BlockType.BRICK
        matrix[18][12] = BlockType.FAST
        matrix[19][12] = BlockType.FAST
        matrix[19][18] = BlockType.BRICK
        matrix[18][18] = BlockType.BRICK
        matrix[17][17] = BlockType.BRICK
        matrix[16][18] = BlockType.FAST
        matrix[16][19] = BlockType.BRICK
        matrix[12][15] = BlockType.BRICK
        matrix[13][15] = BlockType.FAST
        matrix[15][16] = BlockType.BRICK
        matrix[16][17] = BlockType.FAST
        matrix[14][16] = BlockType.BRICK
        matrix[13][19] = BlockType.BRICK
        matrix[13][18] = BlockType.BRICK

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







