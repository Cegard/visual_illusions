from pine import Pine

model = None


def setup():
    global model
    
    size(600, 400, P3D)
    center = PVector(0,0,0)
    model = Pine(8, center, 100, 60)


def draw():
    global model
    
    background(0,0,0)
    lights()
    translate(width/2, height/2)
    model.draw()
    model.turn(1, 0, 0)
    