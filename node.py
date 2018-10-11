class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.x == other.x and self.y == other.y
