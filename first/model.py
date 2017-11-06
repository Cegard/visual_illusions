from transformations import *


class Model:
    
    
    def __make_square(self, height_coef):
        x_coefs = (-1, 1)
        z_coefs = (-1, 1)
        square = []
        calc_component = lambda reference, dimension, distance : \
            reference + dimension*distance/2
        
        for x_coef in x_coefs:
        
            for z_coef in z_coefs:
                x = calc_component(self.center.x, x_coef, self.width)
                y = calc_component(self.center.y, height_coef, self.height)
                z = calc_component(self.center.z, z_coef, self.depth)
                square.append(PVector(x, y, z))
            
            z_coefs = (1, -1)
        
        return square
    
    
    def __build(self):
        index_one, index_two = -1, 0
        self.figure = createShape(GROUP)
        self.figure.disableStyle()
        top_face = make_face(self.__top_square)
        bottom_face = make_face(self.__bottom_square)
        self.figure.addChild(top_face)
        self.figure.addChild(bottom_face)
        
        for square in xrange(4):
            face_points = [self.__top_square[index_one], self.__bottom_square[index_one],
                    self.__bottom_square[index_two], self.__top_square[index_two]]
            face = make_face(face_points)
            self.figure.addChild(face)
            index_one += 1
            index_two += 1
            
    
    
    def __init__(self, center, figure_height, figure_width, figure_depth):
        self.height = figure_height
        self.width = figure_width
        self.depth = figure_depth
        self.center = center
        self.__top_square = self.__make_square(1)
        self.__bottom_square = self.__make_square(-1)
        self.__all_points = self.__top_square + self.__bottom_square
        self.__highests_points = []
        self.__build()
        #self.__stablish_highests()
        self.stroke_weight = 3
        self.line_color = color(255, 255, 0)
        self.face_color = color(0, 255, 255, 100)
        find_core(self.__all_points)
        
        pushMatrix()
        strokeWeight(self.stroke_weight)
        stroke(self.line_color)
        fill(self.face_color)
        popMatrix()
    
    
    def move(self, dx, dy, dz):
        x = self.center.x + dx
        y = self.center.y + dy
        z = self.center.z + dz
        self.center = PVector(x, y, z)
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
    
    
    def turn(self, point_1, point_2, angle):
        angle = radians(angle)
        turn_points(point_1, point_2, angle, self.__all_points)
        self.__build()
    
    
    def draw(self):
        pushMatrix()
        shape(self.figure)
        popMatrix()