from model import Model

model = None
angle = radians(1)
f = None


def setup():
    global model, f
    
    frameRate(100)
    smooth()
    size(800, 600, P3D)
    background(0, 0, 0)
    center = PVector(0, 0, 0)
    model = Model(center, 300, 100, 100)


def draw():
    global model, f
    
    background(0,0,0)
    lights()
    translate(width/2, height/2)
    #model.move(0.6, 0.6, -0.8)
    model.turn('z', 0.01)
    model.turn('x', 0.01)
    model.turn('y', 0.01)
    model.draw()