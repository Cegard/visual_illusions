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
    center = PVector(width/2, height/2, 0)
    model = Model(center, 300, 100, 100)


def draw():
    global model, f
    
    background(0,0,0)
    lights()
    model.move(0.6, 0.6, -0.8)
    model.draw()