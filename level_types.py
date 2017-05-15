import time

class BlockType:
    EMPTY = 0
    AGENT = 1
    OPPONENT = 2
    BRICK = 3
    FAST = 4
    VISTITED = 5

class Direction:
    LEFT = 0
    RIGHT = 1
    DOWN_LEFT = 2
    DOWN_RIGHT = 3
    UP_LEFT = 4
    UP_RIGHT = 5

class Positions:
    AGENT_x = 0
    AGENT_y = 3
    AGENT_direction = Direction.RIGHT

    OPONENT_x = 6
    OPONENT_y = 3
    OPONENT_time = time.clock()
    OPONENT_exist = True
    OPONENT_direction_right = True

