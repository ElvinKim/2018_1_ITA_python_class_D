class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def get(self):
        return self.x, self.y

    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector2D(1, 2)
v2 = Vector2D(1, 2)
v3 = Vector2D(2, 3)

print(v1)
print(v1 == v2)
print(v1 == v3)










