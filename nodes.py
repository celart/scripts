class node():
    def __init__(self):
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
