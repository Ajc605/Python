from york_graphics import *
openWindow()
def face(x, y):

    moveTo(x, y)
    setLineColour('black')
    setFillColour('yellow')
    drawCircle(100)

    setFillColour('yellow')

    moveTo(x, y + 10)
    drawCircle(50)
    setLineColour('yellow')
    moveTo(x, y)
    drawCircle(50)

    setFillColour("black")
    moveTo(x - 50, y - 30)
    drawCircle(10)
    moveTo(x + 50, y - 30)
    drawCircle(10)



face(400,300)
face(150,120)
face(650,500)

updateCanvas()
waitForMouseClick()
