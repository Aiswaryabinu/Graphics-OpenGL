from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

# Number of vertices for blade polygon
n = int(input("Enter the number of vertices: "))
points = []
for i in range(n):
    x, y = map(float, input(f"Enter x,y for vertex {i+1}: ").split())
    points.append((x, y))

angle = 0
speed = 1.5  # rotation speed

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def draw_blade():
    """Draw a single blade polygon"""
    glBegin(GL_POLYGON)
    for item in points:
        glVertex2fv(item)
    glEnd()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the windmill stand (tower)
    glColor3f(0.7, 0.4, 0.1)
    glBegin(GL_POLYGON)
    glVertex2f(-10, -300)
    glVertex2f(10, -300)
    glVertex2f(10, 0)
    glVertex2f(-10, 0)
    glEnd()

    # Move to the pivot point (top of tower)
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glRotatef(angle, 0, 0, 1)

    # Draw 4 rotating blades
    glColor3f(1, 1, 0)
    for i in range(4):
        glPushMatrix()
        glRotatef(i * 90, 0, 0, 1)
        draw_blade()
        glPopMatrix()

    glPopMatrix()

    glFlush()
    glutPostRedisplay()

def update(value):
    global angle
    angle += speed
    if angle >= 360:
        angle = 0
    glutPostRedisplay()
    glutTimerFunc(30, update, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(500, 100)
    glutCreateWindow(b"Windmill Animation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(30, update, 0)
    glutMainLoop()

main()
