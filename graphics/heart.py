from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
scale=0.5
increasing=True
def init():
    glClearColor(0, 0, 0, 1)   # Black background
    gluOrtho2D(-100, 100, -100, 100)

def circle(x_center, y_center, radius):
    glBegin(GL_TRIANGLE_FAN)
    for angle in range(0, 361):
        x = x_center + radius * math.cos(math.radians(angle))
        y = y_center + radius * math.sin(math.radians(angle))
        glVertex2f(x, y)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)   
    glPushMatrix()
    glScalef(scale,scale,1)
    circle(-20, 40, 25)
    circle(20, 40, 25)
    glBegin(GL_TRIANGLES)
    glVertex2f(-43.5, 30)
    glVertex2f(43.5, 30)
    glVertex2f(0, -40)
    glEnd()
    glPopMatrix()
    glFlush()
def animate(value):
    global scale,increasing
    if increasing:
        scale+=0.2
        if scale>=1:
            increasing=False  
    else:
        scale-=0.2
        if scale<=0.5:
            increasing=True
    glutPostRedisplay()
    glutTimerFunc(60,animate,0)        



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Simple Heart")
    glutDisplayFunc(draw)
    glutTimerFunc(60,animate,0)  
    init()
    glutMainLoop()

main()
