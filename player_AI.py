from level_types import*

class player_AI:
    def search(self,matrix,x,y,visitedX,visitedY):
        if matrix[x][y] == BlockType.OPPONENT:
            return True
        elif matrix[x][y] == BlockType.BRICK or matrix[x][y] == BlockType.FAST:
            return False
        elif matrix[x][y] == BlockType.VISTITED:
            return False

        matrix[x][y] = BlockType.VISTITED
        visitedX.append(x)
        visitedY.append(y)
        matrix.__len__()

        if ((x < matrix.__len__() - 1 and self.search(matrix,x + 1, y,visitedX,visitedY))
            or (y > 0 and self.search(x, y - 1))
            or (x > 0 and self.search(x - 1, y))
            or (y < matrix.__len__()- 1 and self.search(matrix,x+1,y,visitedX,visitedY))):
            return True

        return False

