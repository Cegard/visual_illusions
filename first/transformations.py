

__angle_cos = lambda betha: cos(betha)

__angle_sin = lambda betha: sin(betha)

__x_matrix = lambda betha: \
    [
        [1, 0, 0],
        [0, __angle_cos(betha), -__angle_sin(betha)],
        [0, __angle_sin(betha), __angle_cos(betha)]
    ]


__y_matrix = lambda betha: \
    [
        [__angle_cos(betha), 0, __angle_sin(betha)],
        [0, 1, 0],
        [-__angle_sin(betha), 0, __angle_cos(betha)]
    ]


__z_matrix = lambda betha : \
    [
        [__angle_cos(betha), -__angle_sin(betha), 0],
        [__angle_sin(betha), __angle_cos(betha), 0],
        [0, 0, 1]
    ]


def __move_vertex(old_vertex, movement):
    old_vertex.x += movement['x']
    old_vertex.y += movement['y']
    old_vertex.z += movement['z']


def move_points(points, movement):
    
    move = lambda old_point : \
        __move_vertex(old_point, movement)
    
    moved = map(move, points)
    
    return moved


def shear_points(points, movement):
    
    move_point = lambda old_point : __move_vertex(old_point, movement)
    
    sheared = map(move_point, points)
    
    return sheared
    
    
def __scale_vertex(old_point, factors):
    old_point.x *= factors['x']
    old_point.y *= factors['y']
    old_point.z *= factors['z']


def scale_points(points, factors):
    
    _scale = lambda old_point : __scale_vertex(old_point, factors)
    
    scaled = map(_scale, points)
    
    return scaled


###### utilities ######


def obtain_highests(points):
    max_height = float('inf')
    the_highests = []
    
    for actual_point in points:
        point_height = round(actual_point.y, 3)
        
        if (point_height < max_height):
            the_highests = [actual_point]
            max_height = point_height 
        
        elif (point_height == max_height):
            the_highests.append(actual_point)
    
    return the_highests


def make_face(points):
    face = createShape()
    face.beginShape()
    
    for s_point in points:
        face.vertex(s_point.x, s_point.y, s_point.z)
    
    face.endShape(CLOSE)
    
    return face


#######################