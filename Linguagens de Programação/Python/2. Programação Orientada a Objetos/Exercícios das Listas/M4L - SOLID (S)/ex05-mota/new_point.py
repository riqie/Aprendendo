class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, coordx): 
        self.x = coordx 

    def set_y(self, coordy): 
        self.y = coordy

    def get_coords(self):
        return self.x, self.y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def move(self, dx, dy): 
        self.x = dx
        self.y = dy

    def distance(self, dx2, dy2):
        return (self.x - dx2)**2 + (self.y - dy2)**2