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


def multiply_matrices(left_matrix, right_matrix):
    multiplied_matrix = []
    cols = len(right_matrix[0])
    cells = len(right_matrix)
    
    for row in left_matrix:
        col_counter = 0
        result_row = []
        
        for col in xrange(cols):
            cell_counter = 0
            result = 0
            
            for cell in xrange(cells):
                result += row[cell_counter] * \
                          right_matrix[cell_counter][col_counter]
                cell_counter += 1
            
            result_row.append(result)
            col_counter += 1
        
        multiplied_matrix.append(result_row)
    
    return multiplied_matrix


#######################

__x_matrix = lambda cos_betha, sin_betha: \
    [
        [1, 0, 0],
        [0, cos_betha, -sin_betha],
        [0, sin_betha, cos_betha]
    ]


__y_matrix = lambda cos_betha, sin_betha: \
    [
        [cos_betha, 0, sin_betha],
        [0, 1, 0],
        [-sin_betha, 0, cos_betha]
    ]


__z_matrix = lambda cos_betha, sin_betha: \
    [
        [cos_betha, -sin_betha, 0],
        [sin_betha, cos_betha, 0],
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


def scale_points(points, factors, reference_point = None):
    initial_point = reference_point if reference_point else \
                    find_core(points)
    last_point = PVector(-initial_point.x, -initial_point.y,
                         -initial_point.z)
    
    _scale = lambda old_point : __scale_vertex(old_point, factors)
    
    send_to_origin(initial_point, points)
    scaled = map(_scale, points)
    send_to_origin(last_point, points)
    
    return scaled
    
    
def __turn_points(points, turning_matrix):
    
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


def turn_points(point_1, point_2, betha, points,
                reference_point = None):
    initial_point = reference_point if reference_point else \
                        find_core(points)
    last_point = PVector(-initial_point.x, -initial_point.y,
                         -initial_point.z)
    v = point_2 - point_1
    norm_v = v.mag()
    
    a = v.x/norm_v
    b = v.y/norm_v
    c = v.z/norm_v
    d = sqrt(b**2 + c**2)
    
    cos_alpha = c/d
    sin_alpha = b/d
    cos_lambda = d
    sin_lambda = -a
    cos_betha = cos(betha)
    sin_betha = sin(betha)
    
    betha_matrix = __x_matrix(cos_alpha, sin_alpha)
    betha_matrix = multiply_matrices(betha_matrix, 
                                     __y_matrix(cos_lambda, sin_lambda))
    betha_matrix = multiply_matrices(betha_matrix,
                                     __z_matrix(cos_betha, sin_betha))
    betha_matrix = multiply_matrices(betha_matrix, 
                                     __y_matrix(cos_lambda, -sin_lambda))
    betha_matrix = multiply_matrices(betha_matrix,
                                     __x_matrix(cos_alpha, -sin_alpha))
    
    send_to_origin(initial_point, points)
    __turn_points(points, betha_matrix)
    send_to_origin(last_point, points)
    
    
    