from transformations import *

class Pine:
    
    
    def __build(self):
        self.figure = createShape(GROUP)
        self.figure.disableStyle()
        iteration_points = len(self.__base) - 1
        i = 0
        first_face_points = [self.__top, self.__base[0], self.__base[-1]]
        first_face = make_face(first_face_points)
        base = make_face(self.__base)
        self.figure.addChild(first_face)
        self.figure.addChild(base)
        
        while i < iteration_points:
            face_points = [self.__top, self.__base[i], self.__base[i + 1]] 
            face = make_face(face_points)
            self.figure.addChild(face)
            i += 1 
            
    
    def __polygon(self, n, center, figure_height, r):
        angle = 360.0/n
        base = []
    
        for i in xrange(n):
            base.append(PVector(center.x + r * cos(radians(angle * i)), 
                                center.y + figure_height/2,
                                center.z + r * sin(radians(angle * i))))
        
        return base
    
    
    def __init__(self, sides, center, figure_height, base_radius):
        self.core = center
        self.__base = self.__polygon(sides, center, figure_height, base_radius)
        top_y = center.y - figure_height/2
        self.__top = PVector(center.x, top_y, center.z)
        self.__all_points = [self.core, self.__top] + self.__base
        self.__highests_points = []
        self.__build()
        self.stroke_weight = 3
        self.line_color = color(255, 255, 0)
        self.face_color = color(0, 255, 255, 100)
        
        pushMatrix()
        strokeWeight(self.stroke_weight)
        stroke(self.line_color)
        fill(self.face_color)
        popMatrix()
    
    
    def move(self, dx, dy, dz):
        movement = {
            'x' : dx,
            'y' : dy,
            'z' : dz
        }
        move_points(self.__all_points, movement)
        self.__build()
    
    
    def shear(self, dx, dz):
        self.__highests_points = obtain_highests(self.__all_points)
        movement = {
            'x' : dx, 
            'y' : 0, 
            'z' : dz
        }
        shear_points(self.__highests_points, movement)
        self.__build()
    
    
    def scalate(self, sx, sy, sz):
        scale_factors = {
            'x' : sx,
            'y' : sy,
            'z' : sz
        }
        scale_points(self.__all_points, scale_factors)
        self.__build()
    
    
    def turn(self, point_1, point_2, angle, reference_point = None):
        angle = radians(angle)
        turn_points(point_1, point_2, angle, self.__all_points,
                    reference_point)
        self.__build()
  
  
    def draw(self):
        pushMatrix()
        shape(self.figure)
        popMatrix()