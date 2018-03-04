from pine import Pine


def zoom_world(factor):
    global origin, model
    
    origin.z += factor
 
    model.move(0, 0, factor)
    

def rotate_on_x(factor):
    global model
    
    angle = 3*factor
    model.turn_on_x(angle)


model = None
central_angle = 1
orbital_angle = -2
y_angle = 1
zoom = 0
selected = 0
angle = 0
functions = [rotate_on_x, zoom_world]
central_center = PVector(0, 0, 0)
origin = PVector(0,0,0)


def setup():
    global model, central_center, orbital_center
    
    size(800, 600, P3D)
    model = Pine(8, central_center, 180, 80)


def draw():
    global model, central_angle, \
           orbital_angle, y_angle, origin
    
    background(0,0,0)
    lights()
    translate(width/2, height/2)
    rotateX(-frameCount*0.01)
    model.draw()


def keyPressed():
    global origin, functions, selected, angle
    vars = [angle, 0]
    
    if key == ' ':
        selected = (selected+1)%2
    
    elif key == '+':
        
        if selected:
            vars[selected] = 15
        
        else:
            angle -= 1
            vars[selected] = angle
    
    elif key == '-':
        
        if selected:
            vars[selected] = -15
        
        else:
            angle += 1
            vars[selected] = angle
    
    value = vars[selected]
    functions[selected](value)