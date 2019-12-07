class node():
    def __init__(self):
        self.num=None
        self.x=None
        self.y=None
        self.z=None
        self.temp=None

    def setX(self, x):
        self.x=x

    def setY(self, y):
        self.y=y
        
    def setZ(self, z):
        self.z=z
        
    def setT(self, t):
        self.temp=t
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
        
    def getZ(self):
        return self.z
        
    def getT(self):
        return  self.temp
        
    def setNum(self, t):
        self.num=t
        
    def getNum(self):
        return self.num

    def __str__(self):
        return("{0}, {1}, {2}, {3}, {4}".format(self.getNum(), self.getX(), self.getY(), self.getZ(), self.getT()))

