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
    center = PVector(0, 0, 0)
    angle = 0
    model = Model(center, 300, 100, 100)
    #model.turn('x', angle)


def draw():
    global model, f, angle
    
    background(0,0,0)
    lights()
    translate(width/2, height/2)
    model.turn('x', 0.01)
    #model.move(0.6, 0.6, -0.8)
    model.draw()