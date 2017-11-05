

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


def send_to_origin(core, points):
    
    
    def move_to_origin(figure_point):
        figure_point.x -= core.x
        figure_point.y -= core.y
        figure_point.z -= core.z
    
    
    map(move_to_origin, points)


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


def find_core(points):
    x_min, x_max = float('inf'), -float('inf')
    y_min, y_max = float('inf'), -float('inf')
    z_min, z_max = float('inf'), -float('inf')
    
    is_higher = lambda variable, xtreme: \
        variable > xtreme
    
    is_lower = lambda variable, xtreme: \
        variable < xtreme
    
    say_is_xtreme = lambda component, actual, comparator: \
        component if comparator(component, actual) else actual
    
    for figure_point in points:
        x_min = say_is_xtreme(figure_point.x, x_min, is_lower)
        x_max = say_is_xtreme(figure_point.x, x_max, is_higher)
        y_min = say_is_xtreme(figure_point.y, y_min, is_lower)
        y_max = say_is_xtreme(figure_point.y, y_max, is_higher)
        z_min = say_is_xtreme(figure_point.z, z_min, is_lower)
        z_max = say_is_xtreme(figure_point.z, z_max, is_higher)
    
    x_diff = x_min + (x_max - x_min)/2
    y_diff = y_min + (y_max - y_min)/2
    z_diff = z_min + (z_max - z_min)/2
    core = PVector(x_diff, y_diff, z_diff)
    
    return core


#######################