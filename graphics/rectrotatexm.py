from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

theta = 0
wsize = 800

def draw():
    glBegin(GL_QUADS)
    glVertex2f(-100,50)
    glVertex2f(100,50)
    glVertex2f(100,-50)
    glVertex2f(-100,-50)
    glEnd()
def animate():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1,0,0)
    glPushMatrix()
    glRotatef(theta,0,0,1)
    draw()
    glPopMatrix()
    glFlush()
def update(value):
    global theta
    theta+=5
    if theta>=360:
        theta=0
    glutPostRedisplay()
    glutTimerFunc(60,update,0)        


def main():
    glutInit(sys.argv)
    glutInitDisplayMode( GLUT_RGBA)
    glutInitWindowSize(wsize, wsize)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotating Rectangle")
    glutDisplayFunc(animate)
    glutTimerFunc(60, update, 0)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-wsize, wsize, -wsize, wsize)
    glutMainLoop()

main()
