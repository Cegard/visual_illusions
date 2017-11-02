from pine import Pine
from forest import Forest

model = None


def setup():
    global model
    
    size(800, 600, P3D)
    center_1 = PVector(0, 0, 100)
    center_2 = PVector(-150, 0, 0)
    center_3 = PVector(300, 0, -200)
    pine_1 = Pine(8, center_1, 100, 60)
    pine_2 = Pine(8, center_2, 100, 60)
    pine_3 = Pine(8, center_3, 100, 60)
    pines = [pine_1, pine_2, pine_3]
    model = Forest(pines)


def draw():
    global model
    
    background(0,0,0)
    lights()
    translate(width/2, height/2)
    y_angle = 1
    x_shear = cos(radians(y_angle))
    z_shear = sin(radians(y_angle))
    model.shear(x_shear, z_shear)
    model.turn(0, y_angle, 0)
    model.draw()
    #model.turn(1, 0, 0)
    
    