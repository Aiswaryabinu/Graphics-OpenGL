from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

x_pivot = 0
y_pivot = -100
angle = 0
speed = 2
direction = 1
tx=90
x=0

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-300, 300, -300, 300)

def line():
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-20, 190)
    glVertex2f(20, 190)
    glEnd()
def line1():
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(0, 190)
    glVertex2f(x_pivot, y_pivot)
    glEnd()
def line3():
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-300, -160)
    glVertex2f(300, -160)
    glEnd()
def circle():
    glColor3f(0, 0.8, 0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        glVertex2f(x_pivot+30 * math.cos(math.pi * i / 180),
                   y_pivot+30 * math.sin(math.pi * i / 180))
    glEnd()

def circle1():
    glColor3f(0, 0, 0.9)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361):
        glVertex2f(x+40 * math.cos(math.pi * i / 180),
                   -120+40 * math.sin(math.pi * i / 180))
    glEnd()
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    line()
    line3()
    glPushMatrix()
    glTranslatef(x+tx,0,0)
    circle1()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, 190, 0)       # pivot point
    glRotatef(angle, 0, 0, 1)
    glTranslatef(0, -190, 0)
    line1()      # move circle to bottom of the rod
    circle()
    glPopMatrix()
    glFlush()

def animate(value):
    global angle, speed, direction,tx,x
    angle += direction * speed
    if angle >= 60:
        direction = -1
    elif angle <= -60:
        direction = 1
    if angle==0:
        x+=tx
        if x==-300:
            x=0
    
        
    glutPostRedisplay()
    glutTimerFunc(40, animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 30)
    glutCreateWindow(b'Pendulum Animation')
    glutDisplayFunc(draw)
    glutTimerFunc(40, animate, 0)
    init()
    glutMainLoop()

main()
