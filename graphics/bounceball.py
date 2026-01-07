from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

# Global variables
x1, y1 = map(float, input("Enter the center coordinates: ").split())
r = int(input("Enter the radius: "))
ty=0.4
g=-0.8
energy_loss=1
min_velocity=2
is_resting=False
def init():
  glClearColor(0,0,0,1)
  gluOrtho2D(-300,300,-300,300)

def draw():
    global x1, y1
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-200,100)
    glVertex2f(200, 100)
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    
    glVertex2f(x1, y1)
    for i in range(0, 361, 1):
        glVertex2f(x1 + r * math.cos(math.radians(i)),
                   y1 + r * math.sin(math.radians(i)))
    glEnd()
    glFlush()
def translate(value):
    global g,ty,y1,energy_loss,min_velocity,is_resting
    if not is_resting:
        y1+=ty
        ty+=g
        if y1-r<=100:
            y1=100+r
            ty=-ty*energy_loss
            if abs(ty)<min_velocity and y1-r<=50:
                ty=0
                is_resting=True
    glutPostRedisplay()
    glutTimerFunc(30,translate,0)            
            
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
