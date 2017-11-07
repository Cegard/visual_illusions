from model import Model

model = None
angle = 0
f = None


def setup():
    global model, f, angle
    
    frameRate(100)
    smooth()
    size(800, 600, P3D)
    background(0, 0, 0)
    center = PVector(100, 100, 100)
    angle = 0.5
    model = Model(center, 300, 100, 100)
    model.move(0, 200, 0)


def draw():
    global model, f, angle
    
    background(0,0,0)
    lights()
    a = PVector(0,1,0)
    b = PVector(0,2,0)
    model.move(0.5, 0, 0)
    model.turn(a, b, 0.5)
    model.draw()