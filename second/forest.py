class Forest:
    
    
    def __init__(self, pines):
        self.__pines = pines
    
    
    def shear(self, dx, dz):
        
        for pine in self.__pines:
            pine.shear(dx, dz)
    
    
    def turn(self, point_1, point_2, angle):
        
        for pine in self.__pines:
            pine.turn(point_1, point_2, angle)
  
  
    def draw(self):
        
        for pine in self.__pines:
            pine.draw()