from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

# Global variables
x1, y1 = map(float, input("Enter the center coordinates: ").split())
r = int(input("Enter the radius: "))

# Translation step
ty = 0
g=-0.8
ener_loss=0.7
min_velocity = 0.5
is_resting = False


def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw():
    global x1, y1
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(10,50)
    glVertex2f(200,50)
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    
    glVertex2f(x1, y1)
    for i in range(0, 361, 1):
        glVertex2f(x1 + r * math.cos(math.radians(i)),
                   y1 + r * math.sin(math.radians(i)))
    glEnd()
    glFlush()

def translate(value):
    global x1, y1,ty,g,ener_loss,is_resting,r
    if not is_resting:
      y1+=ty
      ty+=g
      if y1-r<=50:
        y1=50+r
        ty=-ty*ener_loss
        
        if abs(ty)<min_velocity and y1 - r <= 50:
            ty=0
            is_resting=True
        
    
            

    glutPostRedisplay()               # redraw with new position
    glutTimerFunc(30, translate, 0)   # call again after 100ms

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b"Moving Ball")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(30, translate, 0)   # start timer
    glutMainLoop()

main()
