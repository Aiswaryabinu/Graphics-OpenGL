import math
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Circle parameters
x1, y1 = map(float, input("Enter circle center (x y): ").split())
r = float(input("Enter circle radius: "))

# Animation variables
dx = 4.0   # speed in x-direction (right)
dy = -3.0  # speed in y-direction (down)
fact_x = -300  # start from left
fact_y = 200   # start from top

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)

def ploat():
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(0, 361):
        angle = math.radians(i)
        glVertex2f(x1 + r * math.cos(angle), y1 + r * math.sin(angle))
    glEnd()
    glFlush()

def animate():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(225/255, 78/255, 31/255)  # orange-red
    glPushMatrix()
    glTranslatef(fact_x, fact_y, 0)  # translate for shooting effect
    ploat()
    glPopMatrix()
    glFlush()

def update(value):
    global fact_x, fact_y, dx, dy

    # Update translation offsets
    fact_x += dx
    fact_y += dy

    # Reset if shooting star goes off screen
    if fact_x > 300 or fact_y < -300:
        fact_x = -300  # start from left
        fact_y = 200   # start from top

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # ~60 FPS

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow(b'Shooting Star')
    init()
    glutDisplayFunc(animate)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()
