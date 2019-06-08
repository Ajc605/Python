from york_graphics import *
openWindow()

def triangle(x1,y1,x2,y2,x3,y3) :
    arrX = [x2 - x1, x3 - x2, x1 - x3]
    arry = [y2 - y1, y3 - y2, y1 - y3]
    setFillColour('white')
    drawCircle(max(arr))
    moveTo(x1,y1)
    drawLine(x2-x1, y2-y1)
    drawLine(x3-x2, y3-y2)
    drawLine(x1-x3, y1-y3)
    # arr = [x2-x1, y2-y1 ,x3-x2, y3-y2, x1-x3, y1-y3]
    # drawCircle(max(arr))

    updateCanvas()

# triangle(200,300,300,200,400,300)


for x in range(3):
    x1, y1 = waitForMouseClick()
    x2, y2 = waitForMouseClick()
    x3, y3 = waitForMouseClick()
    triangle(x1,y1,x2,y2,x3,y3)

waitForMouseClick()