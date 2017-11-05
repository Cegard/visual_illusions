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
    angle = 0.5
    model = Model(center, 300, 100, 100)
    #model.turn(90, 45, 0)
    model.shear(200, -100)
    #model.scalate(2, 0.5, 1)
    #model.turn('x', -angle)


def draw():
    global model, f, angle
    
    background(0,0,0)
    lights()
    translate(width/2, height/2)
    rotateY(radians(frameCount))
    #angle = -angle
    #model.turn('y', angle)
    #model.move(1, 1, 0)
    model.draw()