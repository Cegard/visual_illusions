

class Pine:
    
    
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
    
    
    def __stablish_highests(self):
        max_height = float('inf')
        
        for actual_point in self.__all_points:
            point_height = round(actual_point.y, 3)
            
            if (point_height < max_height):
                self.__highests_points = [actual_point]
                max_height = point_height 
            
            elif (point_height == max_height):
                self.__highests_points.append(actual_point)
    
    
    def __make_face(self, points):
        face = createShape()
        face.beginShape()
        
        for face_point in points:
            face.vertex(face_point.x, face_point.y, face_point.z)
        
        face.endShape(CLOSE)
        
        return face
    
    
    def __build(self):
        self.figure = createShape(GROUP)
        self.figure.disableStyle()
        iteration_points = len(self.__base) - 1
        i = 0
        first_face_points = [self.__top, self.__base[0], self.__base[-1]]
        first_face = self.__make_face(first_face_points)
        base = self.__make_face(self.__base)
        self.figure.addChild(first_face)
        self.figure.addChild(base)
        
        while i < iteration_points:
            face_points = [self.__top, self.__base[i], self.__base[i + 1]] 
            face = self.__make_face(face_points)
            self.figure.addChild(face)
            i += 1 
            
    
    def __polygon(self, n, cx, cz, r):
        angle = 360.0/n
        base = []
    
        for i in xrange(n):
            base.append(PVector(cx + r * cos(radians(angle * i)), 0,
                        cz + r * sin(radians(angle * i))))
        
        return base
    
    
    def __init__(self, sides, center, figure_height, base_radius):
        self.__base = self.__polygon(sides, center.x, center.z, base_radius)
        top_y = -(center.y + figure_height)
        self.__top = PVector(center.x, top_y, center.z)
        
        self.__turning_matrices = {
            'x' : self.__x_matrix,
            'y' : self.__y_matrix,
            'z' : self.__z_matrix,
        }
        self.__all_points = [self.__top] + self.__base
        self.__highests_points = []
        self.__build()
        self.__stablish_highests()
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
    
    
    def __move(self, figure, movement):
        
        move = lambda old_point : \
            self.__move_vertex(old_point, movement)
        
        map(move, self.__all_points)
    
    
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
        self.__move(self.__all_points, movement)
        self.__build()
    
    
    def __turn(self, points, turning_matrix):
        
        turn = lambda old_point, row : \
            old_point.x*row[0] + \
            old_point.y*row[1] + \
            old_point.z*row[2]
        
        
        def turn_point(point_to_turn):
            x = turn(point_to_turn, turning_matrix[0])
            y = turn(point_to_turn, turning_matrix[1])
            z = turn(point_to_turn, turning_matrix[2])
            
            point_to_turn.x = x
            point_to_turn.y = y
            point_to_turn.z = z
        
        
        map(turn_point, points)
            
    
    
    def turn(self, x_angle, y_angle, z_angle):
        x_angle = radians(x_angle)
        y_angle = radians(y_angle)
        z_angle = radians(z_angle)
        x_turning_matrix = self.__turning_matrices['x'](x_angle)
        y_turning_matrix = self.__turning_matrices['y'](y_angle)
        z_turning_matrix = self.__turning_matrices['z'](z_angle)
        self.__turn(self.__all_points, x_turning_matrix)
        self.__turn(self.__all_points, y_turning_matrix)
        self.__turn(self.__all_points, z_turning_matrix)
        self.__build()
    
    
    def __shear(self, points, movement):
        
        move_point = lambda old_point : self.__move_vertex(old_point, movement)
        
        map(move_point, points)
    
    
    def shear(self, dx, dz):
        self.__stablish_highests()
        movement = {
            'x' : dx, 
            'y' : 0, 
            'z' : dz
        }
        self.__shear(self.__highests_points, movement)
        self.__build()
        
        
    def __scale_vertex(self, old_point, factors):
        old_point.x *= factors['x']
        old_point.y *= factors['y']
        old_point.z *= factors['z']
    
    
    def __scalate(self, points, factors):
        
        scalate = lambda old_point : self.__scale_vertex(old_point, factors)
        
        map(scalate, points)
    
    
    def scalate(self, sx, sy, sz):
        scale_factors = {
            'x' : sx,
            'y' : sy,
            'z' : sz
        }
        self.__scalate(self.__all_points, scale_factors)
        self.__build()
  
  
    def draw(self):
        pushMatrix()
        shape(self.figure)
        popMatrix()