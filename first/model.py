

class Model:
    
    
    def __angle_cos(self, betha):
        return cos(betha)
    
    
    def __angle_sin(self, betha):
        return sin(betha)
    
    
    def __x_matrix(self, betha) :
        matrix = [
            [1, 0, 0],
            [0, self.__angle_cos(betha), -self.__angle_sin(betha)],
            [0, self.__angle_sin(betha), self.__angle_cos(betha)]
        ]
        
        return matrix
    
    
    def __y_matrix(self, betha):
        matrix = [
            [self.__angle_cos(betha), 0, self.__angle_sin(betha)],
            [0, 1, 0],
            [-self.__angle_sin(betha), 0, self.__angle_cos(betha)]
        ]
        
        return matrix
    
    
    def __z_matrix (self, betha):
        matrix = [
            [self.__angle_cos(betha), -self.__angle_sin(betha), 0],
            [self.__angle_sin(betha), self.__angle_cos(betha), 0],
            [0, 0, 1]
        ]
        
        return matrix
    
    
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
    
    
    def __stablish_highest(self):
        all_points = self.__top_square + self.__bottom_square
        max_height = -float('inf')
        
        for actual_point in all_points:
            
            if (actual_point.y > max_height):
                self.__highest_points = [actual_point]
                max_height = actual_point.y 
            
            elif (actual_point.y == max_height):
                self.__highest_points.append(actual_point)
            
    
    
    def __init__(self, center, figure_height, figure_width, figure_depth):
        self.height = figure_height
        self.width = figure_width
        self.depth = figure_depth
        self.center = center
        self.__turning_matrices = {
            'x' : self.__x_matrix,
            'y' : self.__y_matrix,
            'z' : self.__z_matrix,
        }
        self.__top_square = self.__make_square(1)
        self.__bottom_square = self.__make_square(-1)
        self.__highest_points = []
        self.__build()
        self.__stablish_highest()
        self.stroke_weight = 3
        self.line_color = color(255, 255, 0)
        self.face_color = color(0, 255, 255, 100)
        
        pushMatrix()
        strokeWeight(self.stroke_weight)
        stroke(self.line_color)
        fill(self.face_color)
        popMatrix()
    
    
    def __move_vertex(self, old_vertex, movement):
        old_vertex.x += movement['x']
        old_vertex.y += movement['y']
        old_vertex.z += movement['z']
    
    
    def __move_square(self, square, movement):
        
        move = lambda old_point : \
            self.__move_vertex(old_point, movement)
        
        square = map(move, square)
    
    
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
    
    
    def __turn_square(self, square, turning_matrix):
        
        for old_point in square:
            x = old_point.x*turning_matrix[0][0] + \
                old_point.y*turning_matrix[0][1] + \
                old_point.z*turning_matrix[0][2]
            
            y = old_point.x*turning_matrix[1][0] + \
                old_point.y*turning_matrix[1][1] + \
                old_point.z*turning_matrix[1][2]
            
            z = old_point.x*turning_matrix[2][0] + \
                old_point.y*turning_matrix[2][1] + \
                old_point.z*turning_matrix[2][2]
            
            old_point.x = x
            old_point.y = y
            old_point.z = z
            
    
    
    def turn(self, axis, angle):
        turning_matrix = self.__turning_matrices[axis](angle)
        self.__turn_square(self.__top_square, turning_matrix)
        self.__turn_square(self.__bottom_square, turning_matrix)
        self.__build()
        self.__stablish_highest()
        if len(self.__highest_points) > 2: print(len(self.__highest_points))
  
  
    def draw(self):
        pushMatrix()
        shape(self.figure)
        popMatrix()