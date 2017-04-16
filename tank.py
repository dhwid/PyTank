from map import *
from PyQt5 import QtCore

class Tank:

    x = Positions.AGENT_x
    y = Positions.AGENT_y
    in_bounds = False


    def check_dimensions(self,dimension):
        if(self.y >=0 and self.x >=0 and self.y < dimension and self.x <dimension):
            in_bounds = True
        else:
            in_bounds = False
        return in_bounds

    def run(self,key,matrix,dimension):

        self.x = Positions.AGENT_x
        self.y = Positions.AGENT_y

        if key == QtCore.Qt.Key_D:
            Positions.AGENT_direction = Direction.RIGHT
            self.y=Positions.AGENT_y+1

            if(self.y < dimension):
                if(matrix[Positions.AGENT_x][self.y]==0):
                    matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
                    matrix[Positions.AGENT_x][self.y] = 1
                    Positions.AGENT_y = self.y


        elif key == QtCore.Qt.Key_A:
            Positions.AGENT_direction = Direction.LEFT
            self.y=Positions.AGENT_y-1
            if(self.y >= 0):
                if(matrix[Positions.AGENT_x][self.y]==0):
                    matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
                    matrix[Positions.AGENT_x][self.y] = 1
                    Positions.AGENT_y = self.y


        elif key == QtCore.Qt.Key_Z:
            Positions.AGENT_direction = Direction.DOWN_LEFT
            if ~self.x % 2:
                self.y = Positions.AGENT_y - 1
            self.x=Positions.AGENT_x+1
            if(self.check_dimensions(dimension)):
                if(matrix[self.x][self.y]==0):
                    matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
                    matrix[self.x][self.y] = 1
                    Positions.AGENT_y = self.y
                    Positions.AGENT_x = self.x

        elif key == QtCore.Qt.Key_C:
            Positions.AGENT_direction = Direction.DOWN_RIGHT
            if self.x % 2:
                self.y=Positions.AGENT_y+1
            self.x=Positions.AGENT_x+1
            if(self.check_dimensions(dimension)):
                if(matrix[self.x][self.y]==0):
                    matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
                    matrix[self.x][self.y] = 1
                    Positions.AGENT_y = self.y
                    Positions.AGENT_x = self.x



        elif key == QtCore.Qt.Key_Q:
            Positions.AGENT_direction = Direction.UP_LEFT
            if ~self.x % 2:
                self.y=Positions.AGENT_y-1
            self.x=Positions.AGENT_x-1
            if(self.check_dimensions(dimension)):
                if(matrix[self.x][self.y]==0):
                    matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
                    matrix[self.x][self.y] = 1
                    Positions.AGENT_y = self.y
                    Positions.AGENT_x = self.x


        elif key == QtCore.Qt.Key_E:
            Positions.AGENT_direction = Direction.UP_RIGHT
            if self.x % 2:
                self.y=Positions.AGENT_y+1
            self.x=Positions.AGENT_x-1
            if(self.check_dimensions(dimension)):
                if(matrix[self.x][self.y]==0):
                    matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
                    matrix[self.x][self.y] = 1
                    Positions.AGENT_y = self.y
                    Positions.AGENT_x = self.x


    def shoot(self,key,matrix,dimension):

        if key == QtCore.Qt.Key_Space:
            if(Positions.AGENT_direction == Direction.RIGHT):
                for j in range(Positions.AGENT_y,dimension):
                    if(matrix[Positions.AGENT_x][j]==BlockType.FAST):
                        break
                    elif(matrix[Positions.AGENT_x][j]==BlockType.BRICK or matrix[Positions.AGENT_x][j]==BlockType.OPPONENT):
                        if matrix[Positions.AGENT_x][j] == BlockType.OPPONENT: Positions.OPONENT_exist = False
                        matrix[Positions.AGENT_x][j] = 0
                        break

            elif (Positions.AGENT_direction == Direction.LEFT):
                for j in range(Positions.AGENT_y, -1,-1):
                    if (matrix[Positions.AGENT_x][j] == BlockType.FAST):
                        break
                    elif (matrix[Positions.AGENT_x][j] == BlockType.BRICK or matrix[Positions.AGENT_x][j] == BlockType.OPPONENT):
                        if matrix[Positions.AGENT_x][j] == BlockType.OPPONENT: Positions.OPONENT_exist = False
                        matrix[Positions.AGENT_x][j] = 0
                        break

            elif (Positions.AGENT_direction == Direction.DOWN_LEFT):
                i=Positions.AGENT_x
                j=Positions.AGENT_y
                while j > 0:
                    if(~i%2): j+=-1
                    i+=1
                    if(i >= dimension):
                        break
                    elif (matrix[i][j] == BlockType.FAST):
                        break
                    elif (matrix[i][j] == BlockType.BRICK or matrix[i][j] == BlockType.OPPONENT):
                        if matrix[i][j] == BlockType.OPPONENT: Positions.OPONENT_exist = False
                        matrix[i][j] = 0
                        break

            elif (Positions.AGENT_direction == Direction.DOWN_RIGHT):
                i=Positions.AGENT_x
                j=Positions.AGENT_y
                while j < dimension:
                    if(i%2): j+=1
                    i+=1
                    if(i >=dimension):
                        break
                    elif (matrix[i][j] == BlockType.FAST):
                        break
                    elif (matrix[i][j] == BlockType.BRICK or matrix[i][j] == BlockType.OPPONENT):
                        if matrix[i][j] == BlockType.OPPONENT: Positions.OPONENT_exist = False
                        matrix[i][j] = 0
                        break

            elif (Positions.AGENT_direction == Direction.UP_LEFT):
                i=Positions.AGENT_x
                j=Positions.AGENT_y
                while j > 0:
                    if(~i%2): j+=-1
                    i+=-1
                    if(i < 0):
                        break
                    elif (matrix[i][j] == BlockType.FAST):
                        break
                    elif (matrix[i][j] == BlockType.BRICK or matrix[i][j] == BlockType.OPPONENT):
                        if matrix[i][j] == BlockType.OPPONENT: Positions.OPONENT_exist = False
                        matrix[i][j] = 0
                        break

            elif (Positions.AGENT_direction == Direction.UP_RIGHT):
                i=Positions.AGENT_x
                j=Positions.AGENT_y
                while j <= dimension:
                    if(i%2): j+=1
                    i+=-1
                    if(i < 0):
                        break
                    elif (matrix[i][j] == BlockType.FAST):
                        break
                    elif (matrix[i][j] == BlockType.BRICK or matrix[i][j] == BlockType.OPPONENT):
                        if matrix[i][j] == BlockType.OPPONENT: Positions.OPONENT_exist = False
                        matrix[i][j] = 0
                        break
