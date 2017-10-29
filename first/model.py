class Model:
    
    
    def __make_square(self, height_coef):
        x_coefs = (-1, 1)
        z_coefs = (-1, 1)
        square = []
        get_point = lambda reference, dimension, length : \
                    reference + dimension*length/2
        
        for x_coef in x_coefs:
            
            for z_coef in z_coefs:
                x = get_point(self.center.x, x_coef, self.width)
                y = get_point(self.center.y, height_coef, self.height)
                z = get_point(self.center.z, z_coef, self.depth)
                square.append(PVector(x, y, z))
            
            z_coefs = (1, -1)
        
        return square
    
    
    def __make_face(self, points):
        face = createShape()
        face.beginShape(QUAD)
        
        for s_point in points:
            face.vertex(s_point.x, s_point.y, s_point.z)
        
        face.endShape(CLOSE)
        
        return face
    
    
    def __build(self):
        index_one, index_two = -1, 0
        self.figure = createShape(GROUP)
        self.figure.disableStyle()
        top_face = self.__make_face(self.__top_square)
        bottom_face = self.__make_face(self.__bottom_square)
        self.figure.addChild(top_face)
        self.figure.addChild(bottom_face)
        
        for quad in xrange(4):
            face_points = [self.__top_square[index_one], self.__bottom_square[index_one],
                           self.__bottom_square[index_two], self.__top_square[index_two]]
            face = self.__make_face(face_points)
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
        self.__build()
    
    
    def __move_square(self, square, movement):
        
        for old_point in square:
            old_point.x += movement['x']
            old_point.y += movement['y']
            old_point.z += movement['z']
    
    
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
        self.__move_square(self.__top_square, movement)
        self.__move_square(self.__bottom_square, movement)
        self.__build()
    
    
    def draw(self):
        pushMatrix()
        stroke_weight = 3
        line_color = color(255, 255, 0)
        face_color = color(0, 255, 255, 100)
        strokeWeight(stroke_weight)
        stroke(line_color)
        fill(face_color)
        shape(self.figure)
        popMatrix()