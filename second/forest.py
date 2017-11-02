class Forest:
    
    
    def __init__(self, pines):
        self.__pines = pines
    
    
    def shear(self, dx, dz):
        
        for pine in self.__pines:
            pine.shear(dx, dz)
    
    
    def turn(self, angle_x, angle_y, angle_z):
        
        for pine in self.__pines:
            pine.turn(angle_x, angle_y, angle_z)
  
  
    def draw(self):
        
        for pine in self.__pines:
            pine.draw()