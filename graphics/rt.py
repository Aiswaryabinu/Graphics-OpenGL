from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

theta = 0
wsize = 800

def drawRectangle():
    glBegin(GL_QUADS)
    glVertex2f(-100, 50)
    glVertex2f(100, 50)
    glVertex2f(100, -50)
    glVertex2f(-100, -50)
    glEnd()

def draw():
    global theta
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)

    glPushMatrix()

    # --- Translation + Rotation combined ---
    radius = 300
    x = radius * math.cos(math.radians(theta))
    y = radius * math.sin(math.radians(theta))
    glTranslatef(x, y, 0)           # move in circular path
    glRotatef(theta, 0, 0, 1)       # rotate rectangle itself

    drawRectangle()
    glPopMatrix()

    glutSwapBuffers()

def animate(temp):
    global theta
    theta += 2
    if theta >= 360:
        theta = 0
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)  # 60 FPS

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(wsize, wsize)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotating and Translating Rectangle")
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-wsize, wsize, -wsize, wsize)
    glutMainLoop()

main()
