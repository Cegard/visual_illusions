from pine import Pine
from forest import Forest

model = None
central_angle = 1
orbital_angle = -2
y_angle = 1
central_center = PVector(150, 0, 0)
orbital_center = PVector(-150, 0, 0)
central = None
orbital = None


def setup():
    global model, central_center, orbital_center, central, orbital
    
    size(800, 600, P3D)
    #rotateX(radians(15))
    central = Pine(8, central_center, 100, 60)
    orbital = Pine(8, orbital_center, 100, 60)
    pines = [central, orbital]
    model = Forest(pines)


def draw():
    global model, central, orbital, central_angle, \
           orbital_angle, y_angle
    
    background(0,0,0)
    lights()
    translate(width/2, height/2)
    # x_shear = cos(radians(y_angle))
    # z_shear = sin(radians(y_angle))
    # model.shear(x_shear, z_shear)
    #model.turn(PVector(0, 1, 0), PVector(0, 2, 0), -y_angle)
    central.move(1, 0, -1)
    central.turn(PVector(0, 1, 0), PVector(0, 2, 0), central_angle,
                 PVector(0,0,0))
    orbital.turn(PVector(0, 1, 0), PVector(0, 2, 0), orbital_angle,
                 central.core)
    model.draw()
    #model.turn(1, 0, 0)